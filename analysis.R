### Analysis of the popularity of r/Hololive ###

### load ggplot2 ###
library(ggplot2)

### load in the csv files containing the data ###
sep2020_posts = read.csv('C:/Users/phill/Desktop/projects/holo/sep2020_post_info.csv')
sep2020_day = read.csv('C:/Users/phill/Desktop/projects/holo/sep2020_day_info.csv')

### line graph of each day of the month ###
a = ggplot(sep2020_posts, aes(x=Date, y=Number.of.Posts, group=1)) +
      geom_line() + geom_path() +
      labs(x='Day of the Month', y='Number of Posts that Day',
           title='Number of Posts Each Day in September 2020') +
      theme(axis.text.x=element_text(size=5),
            plot.title = element_text(hjust = 0.5))

### bar graph of for each day of the week ###
b = ggplot(sep2020_day, aes(Day.of.the.Week, Number.of.Posts, fill=Day.of.the.Week)) +
      geom_col() +
      labs(x='Day of the Week', y='Number of Posts for that Day',
           title='Total Number of Posts for Each Day of the Week') +
      theme(plot.title = element_text(hjust = 0.5))

### getting total count for each type of post ###
flairs = c()
count = c()
for (col in names(sep2020_posts)){
  if (col != 'Date'){
    if (col != 'Number.of.Posts'){
      flairs = c(flairs, col)
      count = c(count, sum(sep2020_posts[[col]]))
    }
  }
}

df = data.frame(Type=flairs, Counts=count)
c = ggplot(df, aes(x=Type, y=Counts, fill=Type)) + 
  geom_col() + theme(axis.text.x=element_text(size=7),
                     plot.title = element_text(hjust = 0.5)) +
  labs(x='Type of Post', title='Count of Each Type of Post in September 2020')

### box plot of the total overall in the month
d = ggplot(sep2020_posts, aes(y=Number.of.Posts)) +
  geom_boxplot() + theme(axis.text.x=element_blank(),
                         axis.ticks.x=element_blank(),
                         plot.title = element_text(hjust = 0.5)) +
  labs(title='Box Plot of the Number of Posts Per Day')
