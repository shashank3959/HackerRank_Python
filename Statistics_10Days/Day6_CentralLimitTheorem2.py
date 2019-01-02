# 10 Days of Statistics: Day 6: Central Limit Theorem 2

import math


mean = 2.4
std = 2.0
n_students = 100
tickets_left = 250

new_mean = mean*n_students
new_std = std*math.sqrt(n_students)

cdf = lambda x: 0.5 * (1 + math.erf((x - new_mean) / (new_std * (2 ** 0.5))))

print("{:.4f}".format(cdf(tickets_left)))
