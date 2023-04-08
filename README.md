# ResearchProjectCrawler
A web crawler I developed to crawl news articles on Irish webpages.

Steps for running the spiders:
  1. Ensure you have scrapy installed and running correctly
  2. Run the command "scrapy crawl SPIDERNAME -o filename.csv"
      Current spider names are: "DublinLive", "TheJournal", "DublinPeople", "IrishTimes"
      ***WARNING: Running the "DublinPeople" spider will take the website down please don't do this until I fix the issue***
 
After running all the spiders running "main.py" will process all the data collected by the spiders.
The processed data is stored in "Ratio.csv" which can be found in the "Articles by location" directory created.
The data comes in the form of {Location}, {Number of articles containing keywords}, {Total number of articles}, {Ratio}

Locations and keywords are stored in the main.py file and can be edited to gain different results.
