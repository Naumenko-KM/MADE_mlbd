#!/usr/bin/python3
"""var_reducer.py"""

import sys


cnt = 0
mean_price = 0
var_price = 0
for line in sys.stdin:
    batch_cnt, batch_mean, batch_var = list(map(float, line.split()))
    var_price = (var_price * cnt + batch_var * batch_cnt) / (batch_cnt + cnt) \
             + cnt * batch_cnt * ((mean_price - batch_mean) / (batch_cnt + cnt)) ** 2
    mean_price = (mean_price * cnt + batch_mean * batch_cnt) / (batch_cnt + cnt)
    cnt += batch_cnt

print(var_price)
