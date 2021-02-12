import pandas as pd
from collections import defaultdict

class HoloCSV():
    def __init__(self, csv_file):
        self.original = pd.read_csv(csv_file)
        self.original = self.original.dropna()
        self.total_posts_dict = defaultdict(int)
        self.day_count_dict = defaultdict(int)
        self.list_of_flairs = ['Subbed/TL', 'Meme', 'Music', 'Streams/Videos', 'Discussion',
                               'Fan Content (OP)', 'Misc.', 'Fan Content (Non-OP)', 'Suggestions', 'Goodies',
                               'NSFW', 'None', 'Special'] # special is for hololive member posts
        self.total_posts_per_day()
        self.post_count_df = self.total_post_df()
        self.new_cols(self.post_count_df)

        self.total_posts_per_day(use='day')
        self.day_count_df = self.total_post_df(use='day')
        self.new_cols(self.day_count_df)

    def get_total_count(self, col, use='date'):
        if use == 'day':
            self.day_count_dict[col] += 1
        else:
            self.total_posts_dict[col] += 1

    def total_posts_per_day(self, use='date'):
        if use == 'day':
            self.original['Day of the Week'].apply(lambda row: self.get_total_count(row, 'day'))
        else:
            self.original['Date'].apply(lambda row: self.get_total_count(row))

    def total_post_df(self, use='date'):
        if use == 'day':
            return pd.DataFrame(self.day_count_dict.items(), columns=['Day of the Week', 'Number of Posts'])
        else:
            return pd.DataFrame(self.total_posts_dict.items(), columns=['Date', 'Number of Posts'])

    def new_cols(self, df):
        for flair in self.list_of_flairs:
            df[flair] = 0

    def flair_count_adder(self, flair, date, use='date'):
        if flair not in self.list_of_flairs:
            flair = 'Special'

        if use == 'day':
            index = self.day_count_df[self.day_count_df['Day of the Week'] == date].index.tolist()
            self.day_count_df.loc[index, flair] += 1
        else:
            index = self.post_count_df[self.post_count_df['Date'] == date].index.tolist()
            self.post_count_df.loc[index, flair] += 1


    def get_individual_flair_count(self, use='date'):
        if use == 'day':
            self.original.apply(lambda row: self.flair_count_adder(row['Flair'], row['Day of the Week'], 'day'), axis=1)
        else:
            self.original.apply(lambda row: self.flair_count_adder(row['Flair'], row['Date']), axis=1)

if __name__ == '__main__':
    file = 'C:/Users/phill/Desktop/projects/holo/hololive_sep_2020.csv'

    testing = HoloCSV(file)
    print(testing.original['Flair'].unique())
    #testing.post_count_df.loc[0, 'Special'] += 1
    testing.get_individual_flair_count()
    testing.post_count_df.to_csv('post_info.csv', encoding='utf-8', index=False)

    #testing.new_cols(testing.day_count_df)
    #print(testing.day_count_df)
    testing.get_individual_flair_count(use='day')
    testing.day_count_df.to_csv('day_info.csv', encoding='utf-8', index=False)
