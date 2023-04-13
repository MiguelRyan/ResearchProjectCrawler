import os
import pandas as pd

os.chdir('..')


class ArticlePruner:
    """Removes all articles from a csv file that do not contain keywords"""

    def __init__(self, directory, keywords, file):
        os.chdir(directory)
        self.keywords = keywords
        self.file = file
        
        # read the CSV file into a DataFrame
        df = pd.read_csv(file)

        # filter the DataFrame to include only rows that contain at least one of the keywords
        try:
            filtered_df = df[df['body'].str.contains('|'.join(keywords), na=False, case=False)]
        except: # Really bad practice
            filtered_df = df[df['text'].str.contains('|'.join(keywords), na=False, case=False)]

        self.number_of_articles = len(df)
        self.number_of_articles_after_pruning = len(filtered_df)
