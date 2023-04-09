import csv
import os
from article_combiner import ArticleCombiner
from article_pruner import ArticlePruner
from article_divider import ArticleDivider

filename = "all_articles"

keywords = ['residential', 'house', 'housing', 'household', 'rehoused', 'homeownership', 'renters', 'properties',
            'immigration', 'immigrant', 'rent', 'apartment', 'segregation', 'discrimination', 'racism', 'prejudice',
            'bias', 'unfairness', 'inequity', 'racial discrimination', 'racial prejudice', 'xenophobia', 'intolerance',
            'developer']

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

ArticleCombiner(os.getcwd(), filename)
ArticleDivider(dublin_locations, filename)

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
