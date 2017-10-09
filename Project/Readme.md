# DVA Project Ren-Turo
Users input their location and budget for buying a car to be rented out.
Based on a regression analysis and similarity scores the top 3 most popular cars for the specifc location within the budget 
will be recommended.

Car features and number of times a car was rented out was scraped from Turo.com (scrape.py).
The average price of the car was scraped from Autotrader.com (GetUsedCarProces.py).
The regrssion analysis was done on the features to rank important features of the cars using reg.py.
After weighing the important features a score for each car was calculated. The higher the score the more popular the car. 
Using euclidean distance (sim.py) the final list of cars was output.
