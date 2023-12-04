# sc-capstone

Topic is "how to evaluate what a winning investment strategy is for buying stocks associated with companies that develop electric vehicles.

**Sharpe Ratio evaluation for Tesla versus competitors**


Sharpe ratio

*The Sharpe ratio (or Sharpe Index) is named after its creator William Sharpe, the 1990 winner of the Nobel Prize in economic sciences. It is a measure of investment portfolio performance. The Sharpe ratio represents the return of a portfolio, without taking into account the “risk-free” interest rate and indicates the return percentage for each risk unit carried by the investment.

Using the Sharpe ratio as part of your fundamental analysis strategy​ helps to provide important financial information that can be used to make smarter trading decisions. (from https://www.cmcmarkets.com/en/trading-guides/the-sharpe-ratio-definition#:~:text=A%20Sharpe%20ratio%20less%20than,amount%20of%20investment%20risk%20taken.)

Method to calculate Sharpe ratio using python comes from https://projects.datacamp.com/projects/66

Daily data is coming from https://finance.yahoo.com/quote/TSLA/history?p=TSLA  First pass data was exported on 9-Nov-2023.  I may do another pass where I download it for the day with web scraping.  That would be cool!

List of Tesla competitors came from here:  https://money.usnews.com/investing/stock-market-news/slideshows/upstart-tesla-competitors-to-watch

Great article on data cleaning:  https://towardsdatascience.com/data-cleaning-with-python-and-pandas-detecting-missing-values-3e9c6ebcf78b#:~:text=Using%20the%20isnull()%20method,NA%E2%80%9D%20types%20as%20missing%20values.
