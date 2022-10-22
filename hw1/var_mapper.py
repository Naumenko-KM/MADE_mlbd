#!/usr/bin/python3
"""var_mapper.py"""

import sys
import csv

PRICE_COL = 9

var = 0
prices = []
for line in csv.reader(sys.stdin):
    price = line[PRICE_COL]
    if price == 'price':
        continue
    prices.append(int(price))

mean_price = sum(prices) / len(prices)

for price in prices:
    var += (price - mean_price) ** 2
var = var / len(prices)

print(len(prices), mean_price, var)