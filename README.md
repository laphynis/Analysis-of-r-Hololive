In this project, I will be collecting data from the Hololive subreddit (https://www.reddit.com/r/Hololive/) and performing some analysis through visualizations. Currently, I only have data for September 2020, but I am planning to collect data in March 2021 for a comparison in growth.

# Collecting the Data
To collect the data, I used the Reddit API (PRAW) to collect data directly from Reddit and Google Sheets API to write and maintain a spreadsheet with the data that I am collecting. The script that I wrote extracts various information from the newest submissions, most notably the date, the type of post (flair), and the day of the week. However, there is a limit to the number of API calls for both Reddit and Google Sheets, so I coded my script to check the three newest submissions every 30 seconds and ignore duplicates. Lastly, in order to run this script continuously, I utilized PythonAnywhere (https://www.pythonanywhere.com/) to run my script during the night when my computer is off. My data collecting script can be found in the r-hololive data collection.py

# Cleaning the Data
After exporting my spreadsheet as a csv file, I made a script to manipulate the data in the csv file into a usable format. My data was in individual entries, but I wanted it to contain data of a count for the number of posts for a day of the month, day of the week, type of post, etc. In order to do this, I mainly used the pandas library for my dataframe manipulation. I created a class, so that I would be able to quickly clean my data again if I were to collect data on the subreddit again. The code can be found in the cleaning.py file.

# Visualizing Trends
For visualizing data, I used R's ggplot2 library. The code can be found in the analysis.R file.

Right off the bat, I wanted to see how the number of posts per day changed throughout the month. To visualize this, I plotted a lineplot.

<img src="/Graphs/day_count.png" width="800" height="400">


From the lineplot above, there doesn't appear to be any pattern. The number of posts per day seem to fluctuate and is hard to predict. However, there is a reason as to why there are two large peaks which would only be known to someone who browses the subreddit. The first peak is due to the announcement of the Hololive English branch, and the second is due to a major controversy. However, outside of these rare events, it looks subreddit popularity remains relatively stable. 

