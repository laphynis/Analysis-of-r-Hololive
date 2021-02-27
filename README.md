In this project, I will be collecting data from the Hololive subreddit (https://www.reddit.com/r/Hololive/) and performing some analysis through visualizations. 

# Collecting the Data
To collect the data, I used the Reddit API (PRAW) to collect data directly from Reddit and Google Sheets API to write and maintain a spreadsheet with the data that I am collecting. The script that I wrote extracts various information from the newest submissions, most notably the date, the type of post (flair), and the day of the week. However, there is a limit to the number of API calls for both Reddit and Google Sheets, so I coded my script to check the three newest submissions every 30 seconds and ignore duplicates. Lastly, in order to run this script continuously, I utilized PythonAnywhere (https://www.pythonanywhere.com/) to run my script during the night when my computer is off. My data collecting script can be found in collection.py

# Cleaning the Data
After exporting my spreadsheet as a csv file, I made a script to manipulate the data in the csv file into a usable format. My data was in individual entries, but I wanted it to contain data of a count for the number of posts for a day of the month, day of the week, type of post, etc. In order to do this, I mainly used the pandas library for my dataframe manipulation. I created a class, so that I would be able to quickly clean my data again if I were to collect data on the subreddit again. The code can be found in cleaning.py.

# Visualizing Trends
For visualizing data, I used R's ggplot2 library. The code can be found in the analysis.R file.

Right off the bat, I wanted to see how the number of posts per day changed throughout the month. To visualize this, I plotted a lineplot.

<img src="/Graphs/day_count.png" width="800" height="400">


From the lineplot above, there doesn't appear to be any pattern. The number of posts per day seem to fluctuate and is hard to predict. Although there are two peaks in the plot, the first can be explained by the announcement of the Hololive English branch which many people were excited for, and the second can be explained by a controversy that angered many people. Outside of these rare events, the number of posts seem to be growing, albeit not as much.  

The next thing that I want to look at is the total number of posts distributed throughout the days of the week. Even before visualizing the data, I assumed that the weekend (Friday, Saturday, and Sunday) would have a significantly higher average of new submissions since there will be more people with free time. To investigate this, I created a plot of several boxplots, each boxplot corresponding to a day of the week. 

<img src="https://cdn.discordapp.com/attachments/809997123893461002/809997233567039488/dotw_boxplots_2020-1.png" width="800" height="400">

Surprisingly, the average number of posts on Fridays and Saturdays are about the same as the other days besides Sunday. However, if we look at the maximum for both the boxplots of Saturday and Sunday, we can see that there is at least one Saturday and one Sunday that had significantly more posts than any other day of the week in September 2020. Overall, my assumption was correct that weekend should have higher number of posts with the exception of Friday being much lower than anticipated. 

Next, I want to take a look at the proportion of post types (flairs). 

<img src="/Graphs/flair_count.png" width="800" height="400">

Right away, we can see that the number of "Meme" posts significantly tower over the other types. To be precise, out of 33297 posts, 17236 of those posts were memes. In terms of percentage, thats about 51.76%. So based on the data, almost half of the posts being made in the subreddit are memes!

Now, doing the same process as before, I want to see the number of memes being posted for each day of the week. Perhaps some days have a higher volume of memes being posted. Once again, I assumed that the weekend days (Friday, Saturday, Sunday) will have a higher number of memes posted for similar reasons as stated before. However, from the results of the previous boxplots, I doubt Friday will not have as many memes as Saturday or Sunday. 

<img src="https://cdn.discordapp.com/attachments/809997123893461002/810002833129603082/dotw_memes-1.png" width="800" height="400">

Not surprisingly, the boxplots for memes are quite similar in shape compared to the boxplots for the total number of posts. Once again, Saturday and Sunday have the highest maximum. However, this time, there are outliers on Saturday and Thursday. 

In conclusion, there doesn't seem to be any signs of large growth on the Hololive subreddit based on the number of submissions throughout the month of September 2020 when excluding the two major events that occurred during that month. However, from this analysis, I found out that memes make up about half of the number of posts made on the subreddit. This is a pretty large number especially since there are over a dozen different flairs to use. I knew that many memes were being posted, but I did not know it was to this extent. 
