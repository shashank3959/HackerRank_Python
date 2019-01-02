# 10 Days of Statistics: Day 6: Central Limit Theorem 1

import math

max = 9800
n_boxes = 49
mean = 205
std = 15

new_mean = mean*n_boxes
new_std = std*math.sqrt(n_boxes)

cdf = lambda x: 0.5 * (1 + math.erf((x - new_mean) / (new_std * (2 ** 0.5))))

print("{:.4f}".format(cdf(9800)))