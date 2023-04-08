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

dublin_locations = ["Ardlea", "Arklow", "Artane", "Ashford", "Athy", "Aughrim", "Aughrim Street", "Avoca",
                    "Ayrfield", "Balally", "Balbriggan", "Balcurris", "Baldoyle", "Ballinteer", "Ballyboden",
                    "Ballybrack", "Killiney", "Ballyfermot", "Ballygall", "Ballymore Eustace", "Ballymun",
                    "Ballyroan", "Bawnogue", "Bayside", "Beaumont", "Beechwood Avenue", "Berkeley Road",
                    "Blackrock", "Blakestown", "Blanchardstown", "Blessington", "Bluebell", "Bohernabreena",
                    "Bonnybrook", "Booterstown", "Brackenstown", "Bray", "Brookfield", "Cabinteely", "Cabra",
                    "Castledermot", "Castleknock", "Castletown", "Celbridge", "Chapelizod", "Cherry Orchard",
                    "Churchtown", "City Quay", "Cloger Road", "Clondalkin", "Clonskeagh", "Clontarf", "Confey",
                    "Coolock", "Corduff", "Crumlin", "Dalkey", "Darndale", "Deansrath", "Dollymount", "Dolphins Barn",
                    "Dominick Street", "Donabate", "Donaghmede", "Donnybrook", "Donnycarney", "Donore Ave",
                    "Drumcondra", "Dun Laoghaire", "Dundrum", "Dunlavin", "Eadestown", "East Wall", "North Strand",
                    "Edenmore", "Enniskerry", "Esker", "Dodsboro", "Adamstown", "Fairview", "Finglas", "Firhouse",
                    "Foxrock", "Francis Street", "Gardiner Street", "Garristown", "Glasnevin", "Glasthule",
                    "Glendalough", "Grange Park", "Greenhills", "Greystones", "Haddington Road", "Halston Street",
                    "Harolds Cross", "Harrington Street", "Hartstown", "Howth", "Huntstown", "Inchicore", "Iona Road",
                    "Jobstown", "Johnstown", "Kilbarrack", "Kilbride", "Barndarrig", "Kilcullen", "Killester",
                    "Killinarden", "Kill-O'-The-Grange", "Kilmacud", "Stillorgan", "Kilmore Road West", "Kilnamanagh",
                    "Kilquade", "Kimmage Manor", "Kinsealy", "Knocklyon", "Larkhill", "Whitehall", "Santry",
                    "Carpenterstown", "Leixlip", "Little Bray", "Loughlinstown", "Lucan", "Lusk", "Malahide",
                    "Marino", "Marley Grange", "Maynooth", "Meadowbrook", "Meath Street", "Merchants Quay",
                    "Merrion Road", "Milltown", "Monkstown", "Moone", "Mount Argus", "Mount Merrion", "Mount View",
                    "Mourne Road", "Mulhuddart", "Narraghmore", "Naul", "Navan Road", "Neilstown", "Newcastle",
                    "Newtownpark", "North William Street", "Palmerstown", "Phibsboro", "Porterstown", "Clonsilla",
                    "Portmarnock", "Priorswood", "Pro Cathedral", "Raheny", "Rathdrum", "Rathfarham", "Rathgar",
                    "Rathmines", "Rialto", "Ringsend", "River Valley", "Rivermount", "Rolestown", "Roundwood",
                    "Rowlagh", "Rush", "Saggart", "Sallynoggin", "Sandyford", "Sandymount", "Sean Mc Dermott Street",
                    "Seville Place", "Shankill", "Silloge", "Skerries", "Springfield", "Sruleen", "Sutton", "Swords",
                    "Tallaght", "Templeogue", "Terenure", "Newman University Church", "Valleymount", "Walkinstown",
                    "Westland Row", "Whitefriar Street", "Wicklow", "Willington", "James's Street", ]

ArticleCombiner(os.getcwd(), filename)
ArticleDivider(dublin_locations, filename)

os.chdir("Articles by location")

with open("Ratio.csv", "w", encoding="UTF-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Location", "Number of Articles After Pruning", "Number of Articles", "Ratio"])

    for file in os.listdir(os.getcwd()):
        if file == "Ratio.csv":
            continue
        ap = ArticlePruner(keywords, file)
        row = [file[:-13], ap.number_of_articles_after_pruning, ap.number_of_articles, ap.number_of_articles_after_pruning / ap.number_of_articles]
        print(row)
        writer.writerow(row)




