# DVA Project Ren-Turo
Given a budget and location predicts the top 3 cars which if rented out to customers will produce the most revenue.
Predictions are based off on previous car rental data on Turo.com

Car features and number of times a car was rented out was scraped from Turo.com (scrape.py).
The average price of the car was scraped from Autotrader.com (GetUsedCarProces.py).
The regrssion analysis was done on the features to rank important features of the cars using reg.py.
After weighing the important features a score for each car was calculated. The higher the score the more popular the car. 
Using euclidean distance (sim.py) the final list of cars was output.
