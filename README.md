# sc-capstone

The updated question I want to ask is "how do AirBnB rental rates and prices correlate with house sales and rental prices in Chicago over time".

Mural board about the topic is:  https://app.mural.co/t/eyatzeck9578/m/eyatzeck9578/1696981775277/b5da6df705ca55cedd763367fd0fe45e8bc6d4e8?sender=ud56793e22b030d91cd068161

Primary sources for data are here:  
* Cook county price indices quarterly since 1997:  https://price-index.housingstudies.org/
* AirBnB data for Chicago going back a year:  http://insideairbnb.com/get-the-data (pull multiple files for Chicago to get four quarters)
* Rental comparisons year on year:  https://www.apartmentguide.com/blog/average-rent-in-chicago/

Approach:
* Combine data from the three sources to get year on year information for AirBnB, rentals, and sales prices
   * stretch goal -- screen scrape to get the data from the pages where it is on the screen, as opposed to provided in file format
   * do somthing in excel or sql.  Maybe initial analysis in excel to establish common language across data sets
   * import all three
   * massage in python  establish commonality for time frames and neighborhood names
   * export to csv
   * visualize in Tableau, looking for different patterns in different neighborhoods
