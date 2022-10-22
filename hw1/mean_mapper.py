#!/usr/bin/python3
"""mean_mapper.py"""

import sys
import csv

PRICE_COL = 9

prices = []
for line in csv.reader(sys.stdin):
    price = line[PRICE_COL]
    if price == 'price':
        continue
    prices.append(int(price))

print(len(prices), sum(prices) / len(prices))

