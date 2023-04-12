import json
import csv
import os

class JsonToCsv():
    """Takes json file as input and creates a csv of the file."""
    def __init__(self, directory, json_file, csv_file_name):
        os.chdir(directory)

        with open(json_file, "r") as f:
            data = json.load(f)

        with open(csv_file_name, "w", encoding="UTF-8", newline="") as f:
            csv_writer = csv.writer(f)

            header = list(data[0].keys())
            csv_writer.writerow(header)

            for line in data:
                row = []
                for key in header:
                    value = line.get(key, '')
                    if isinstance(value, list):
                        value = '|'.join([str(v) for v in value])
                    elif not isinstance(value, str):
                        value = " "
                    row.append(value)
                csv_writer.writerow(row)

