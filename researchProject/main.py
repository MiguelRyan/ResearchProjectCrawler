import csv
import os
from article_combiner import ArticleCombiner
from article_pruner import ArticlePruner
from article_divider import ArticleDivider
from json_reader import JsonToCsv

keywords = ['residential', 'house', 'housing', 'household', 'rehoused', 'homeownership', 'renters', 'properties',
            'immigration', 'immigrant', 'migrant', 'migration', 'rent', 'apartment', 'segregation', 'discrimination',
            'racism', 'prejudice', 'bias', 'unfairness', 'inequity', 'racial discrimination', 'racial prejudice',
            'xenophobia', 'intolerance', 'developer']

dublin_locations = ["ARRAN QUAY", "ASHTOWN", "AYRFIELD", "BALLYBOUGH", "BALLYGALL", "BALLYMUN", "BEAUMONT",
                    "BOTANIC", "CABRA", "CLONTARF", "DRUMCONDRA", "EDENMORE", "FINGLAS", "GRACE PARK", "GRANGE",
                    "HARMONSTOWN", "INNS QUAY", "KILMORE", "MOUNTJOY", "NORTH DOCK", "PHOENIX PARK", "PRIORSWOOD",
                    "RAHENY", "ROTUNDA", "WHITEHALL", "CHAPELIZOD", "CHERRY ORCHARD", "CRUMLIN", "DECIES", "DRUMFINN",
                    "INCHICORE", "KILMAINHAM", "KIMMAGE", "KYLEMORE", "MANSION HOUSE", "MERCHANTS", "PEMBROKE",
                    "RATHFARNHAM", "RATHMINES", "ROYAL EXCHANGE", "ST KEVIN'S", "SOUTH DOCK", "TERENURE", "USHERS",
                    "WALKINSTOWN", "WOOD QUAY", "BALLINASCORNEY", "BALLYBODEN", "BOHERNABREENA", "CLONDALKIN",
                    "EDMONDSTOWN", "FIRHOUSE", "LUCAN", "NEWCASTLE", "PALMERSTON VILLAGE", "PALMERSTON WEST",
                    "RATHCOOLE", "RATHFARNHAM", "SAGGART", "TALLAGHT", "TEMPLEOGUE", "TERENURE", "BALBRIGGAN",
                    "BALDOYLE", "BALGRIFFIN", "BALLYBOGHIL", "BALSCADDEN", "BLANCHARDSTOWN", "CASTLEKNOCK",
                    "CLONMETHAN", "DONABATE", "DUBBER", "GARRISTOWN", "HOLLYWOOD", "HOLMPATRICK", "HOWTH",
                    "KILSALLAGHAN", "KINSALEY", "LUSK", "MALAHIDE", "PORTMARNOCK", "RUSH", "SKERRIES", "SUTTON",
                    "SWORDS", "TURNAPIN", "BALLINTEER", "BALLYBRACK", "BLACKROCK", "CABINTEELY", "CHURCHTOWN",
                    "CLONSKEAGH", "DALKEY", "DUNDRUM", "DUN LAOGHAIRE", "FOXROCK", "GLENCULLEN", "KILLINEY",
                    "SHANKILL", "STILLORGAN", "TIBRADDEN"]

working_directory = os.getcwd()

# Change these values to run respective parts of the code.
NEWS_DATA_WRANGLER = False
NEWS_CREATE_RATIOCSV = False
TWITTER_DATA_WRANGLER = False
TWITTER_CREATE_RATIOCSV = True

if NEWS_DATA_WRANGLER:
    directory = os.path.join(working_directory, "News Article Data")
    filename = "all_articles"

    ArticleCombiner(directory, filename)
    ArticleDivider(directory, dublin_locations, filename, "Articles by location")

if NEWS_CREATE_RATIOCSV:
    os.chdir("Articles by location")
    output_dir = os.path.abspath(os.path.join(os.getcwd(), "..", "data"))
    output_file = 'Ratios.csv'

    with open(os.path.join(output_dir, output_file), mode='w', newline='') as output_csv:
        writer = csv.writer(output_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        writer.writerow(["Location", "Number of articles contained keywords", "Total number of articles", "Ratio"])

        # Write data to the output file
        for file in os.listdir(os.getcwd()):
            ap = ArticlePruner(keywords, file)
            row = [file[:-13].upper(), ap.number_of_articles_after_pruning, ap.number_of_articles, ap.number_of_articles_after_pruning / ap.number_of_articles]
            writer.writerow(row)

if TWITTER_DATA_WRANGLER:
    directory = os.path.join(working_directory, "Twitter Data")
    filename = "all_twitter_data"
    JsonToCsv(directory, "makeireland_safe_again.json", "twitter_data_makeirelandsafeagain.csv")
    JsonToCsv(directory, "ireland_is_full.json", "twitter_data_irelandisfull.csv")
    ArticleCombiner(directory, "all_twitter_data.csv")
    ArticleDivider(directory, dublin_locations, filename, "Tweets by location")

if TWITTER_CREATE_RATIOCSV:
    directory = os.path.join(working_directory, "Twitter Data")
    os.chdir(os.path.join(directory, "Tweets by location"))
    output_file = 'Ratios.csv'

    with open(os.path.join(directory, output_file), mode='w', newline='') as output_csv:
        writer = csv.writer(output_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        writer.writerow(["Location", "Number of articles contained keywords", "Total number of articles", "Ratio"])

        # Write data to the output file
        for file in os.listdir(os.getcwd()):
            ap = ArticlePruner(keywords, file)
            row = [file[:-13].upper(), ap.number_of_articles_after_pruning, ap.number_of_articles,
                   ap.number_of_articles_after_pruning / ap.number_of_articles]
            writer.writerow(row)
