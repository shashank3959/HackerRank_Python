# 10 Days of Statistics: Day 6: Central Limit Theorem 3

import math


zScore = 1.96
std = 80
n = 100
mean = 500
marginOfError = zScore * std / math.sqrt(n)
print(mean - marginOfError)
print(mean + marginOfError)

