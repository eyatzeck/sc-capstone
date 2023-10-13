# sc-capstone

The question I want to ask is "are airfare prices lower for long haul flights, mile for mile, than short haul".

Mural board about the topic is:  https://app.mural.co/t/eyatzeck9578/m/eyatzeck9578/1696981775277/b5da6df705ca55cedd763367fd0fe45e8bc6d4e8?sender=ud56793e22b030d91cd068161

Primary source for data is here:  https://www.transportation.gov/policy/aviation-policy/domestic-airline-consumer-airfare-report

Data is published monthly in pdf form, so one thing I will need to do is figure out how to get the file (stretch goal -- most recent) and parse the PDF for data before cleaning it.

Approach:
* start by getting the data for one month out of one PDF.  Clean it and do all the other mandatory steps for the capstone.
  * I think that includes getting the stats on the set, dealing with missing values, finding outliers, etc.
  * I think there is a mandatory use of sql or excel -- figure out a way to use sql.
* assess whether I can find and parse the pdf in situ on the web all in one go, or if it is a two step process to find, download, and parse.
  * based on assessment, do either one-step or two-step version
* it would be nice to be able to compare these over time, so repeat the process for 1-n pdf files on the site
* stretch goal -- go find out which is the most recent and whether I have it or not in the database; pull it down.
* Tableau integration is a bit down the road, but I could iterate on that as well. 
* I started playing with BeautifulSoup for web parsing, for step 2, but before I do more of that, I want to see about doing the really basic data analysis stuff off of a pre-parsed file.
