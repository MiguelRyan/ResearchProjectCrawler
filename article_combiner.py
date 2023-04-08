import pandas as pd
import glob


class ArticleCombiner:
    """Piece of code that can combine a bunch of csv's into one file"""

    def __init__(self, directory, output_file_name):
        # Move the directory up one to where the csv files are saved
        self.directory = directory
        self.output_file_name = output_file_name

        # Select all csv files
        csv_files = glob.glob('*.csv')

        # Create an empty list to store the dataframes
        dfs = []

        # Loop through each CSV file and read it into a dataframe
        for file in csv_files:
            df = pd.read_csv(file)
            dfs.append(df)

        # Concatenate all the dataframes into a single dataframe
        combined_df = pd.concat(dfs, ignore_index=True)

        # Write the combined dataframe to a new CSV file
        combined_df.to_csv(f'{output_file_name}.csv', index=False)
