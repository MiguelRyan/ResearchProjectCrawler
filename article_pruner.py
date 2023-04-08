import os
import pandas as pd

os.chdir('..')


class ArticlePruner:
    """Removes all articles from a csv file that do not contain keywords"""

    def __init__(self, keywords, filename, output_file_name):
        self.keywords = keywords
        self.filename = filename

        # read the CSV file into a DataFrame
        df = pd.read_csv(f"{filename}.csv")

        # filter the DataFrame to include only rows that contain at least one of the keywords
        filtered_df = df[df['body'].str.contains('|'.join(keywords))]

        # write the filtered DataFrame back to a CSV file
        filtered_df.to_csv(f'{output_file_name}.csv', index=False)
