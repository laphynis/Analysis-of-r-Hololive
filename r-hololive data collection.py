import praw
import datetime
import calendar
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#connecting to reddit API
reddit = praw.Reddit(client_id='REDDIT CLIENT ID HERE',
                     client_secret='REDDIT CLIENT SECRET HERE',
                     user_agent='USER_AGENT HERE')
#connecting to the hololive subreddit
hololive = reddit.subreddit('hololive')

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file',
         'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('CREDS.json HERE', scope)

client = gspread.authorize(creds)

#open up the google sheet
sheet = client.open('GOOGLE SHEET NAME HERE').sheet1

#indefinite loop that keeps checking new posts
while True:
    #checking the first three new submissions
    for post in hololive.new(limit=3):
        
        #list of existing ids in the google sheet
        list_of_ids = [ids for ids in sheet.col_values(4) if ids][:50]
        post_id = str(post.id)
        
        #check if the post id already exists in the sheet
        if post_id in list_of_ids:
            continue
        
        #if not, get all the relevant data and insert a new row
        else:
            #creating an empty list that the info will be appended to
            list_of_info = []

            #getting the info of the post
            title = str(post.title)
            flair = str(post.link_flair_text)
            post_author = str(post.author)
            url_link = str(post.permalink)
            text_post = str(post.is_self)
            distinguished_post = str(post.distinguished) 

            #getting the time of creation for the post and converting from unix
            time_created = post.created_utc
            timestamp = datetime.datetime.fromtimestamp(time_created)
            date = timestamp.strftime('%Y-%m-%d')
            time_made = timestamp.strftime('%H:%M:%S')
            day_of_the_week = timestamp.strftime('%A')
            
            #appending all the info into a list
            list_of_info.extend([date, time_made, title, post_id,
                                post_author, flair, url_link,
                                 text_post, distinguished_post,
                                 day_of_the_week])

            #inserts the list of info into the google sheet
            sheet.insert_row(list_of_info, 2)
            
    #wait 30 seconds before checking new submissions again
    time.sleep(30)
