#!/usr/bin/python3
"""mean_reducer.py"""

import sys

mean_prices = []
cnt = 0
mean_price = 0
for line in sys.stdin:
    batch_cnt, batch_price = list(map(float, line.split()))
    mean_price = (mean_price * cnt + batch_price * batch_cnt) / (batch_cnt + cnt)
    cnt += batch_cnt

print(mean_price)
