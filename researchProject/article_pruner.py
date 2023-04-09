import os
import pandas as pd

os.chdir('..')


class ArticlePruner:
    """Removes all articles from a csv file that do not contain keywords"""

    def __init__(self, keywords, file):
        self.keywords = keywords
        self.file = file

        # read the CSV file into a DataFrame
        df = pd.read_csv(file)

        # filter the DataFrame to include only rows that contain at least one of the keywords
        filtered_df = df[df['body'].str.contains('|'.join(keywords), na=False)]

        self.number_of_articles = len(df)
        self.number_of_articles_after_pruning = len(filtered_df)
