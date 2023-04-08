import csv
import os


class ArticleDivider:
    """Class that divides the main csv into multiple based on location"""

    def __init__(self, locations, file):
        self.locations = locations
        self.file = file

        # Create a folder for our locations
        if not os.path.exists('Articles by location'):
            os.makedirs('Articles by location')

        # Open the main csv file
        with open(f'{file}.csv', 'r', encoding="utf8") as csvfile:
            reader = csv.DictReader(csvfile)

            # Create a dictionary to store the articles for each keyword
            articles_by_location = {}
            for location in locations:
                articles_by_location[location] = []

            # Iterate over each row in the CSV file
            for row in reader:
                text = row['body']

                # Check if any of the locations are present in the text
                for location in locations:
                    if location in text:
                        articles_by_location[location].append(row)

            # Save the articles for each location to separate CSV files if the articles exist
            for keyword, articles in articles_by_location.items():
                if articles:
                    output_file = os.path.join('Articles by location', f'{keyword}_articles.csv')
                    with open(output_file, 'w', newline='', encoding="utf8") as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames=reader.fieldnames)
                        writer.writeheader()
                        writer.writerows(articles)
