# Objective
# In
# this
# challenge, you
# 'll work with arithmetic operators. Check out the Tutorial tab for learning materials and an instructional video!
#
# Task
# Given
# the
# meal
# price(base
# cost
# of
# a
# meal), tip
# percent(the
# percentage
# of
# the
# meal
# price
# being
# added as tip), and tax
# percent(the
# percentage
# of
# the
# meal
# price
# being
# added as tax) for a meal, find and print the meal's total cost.
#
# Note: Be
# sure
# to
# use
# precise
# values
# for your calculations, or you may end up with an incorrectly rounded result!
#
# Input
# Format
#
# There
# are
# lines
# of
# numeric
# input:
# The
# first
# line
# has
# a
# double, (the cost of the meal before tax and tip).
# The
# second
# line
# has
# an
# integer, (the percentage of  being added as tip).
# The
# third
# line
# has
# an
# integer, (the percentage of  being added as tax).
#
# Output
# Format
#
# Print
# The
# total
# meal
# cost is totalCost
# dollars., where is the
# rounded
# integer
# result
# of
# the
# entire
# bill(
# with added tax and tip).
#
# Sample
# Input
#
# 12.00
# 20
# 8
# Sample
# Output
#
# The
# total
# meal
# cost is 15
# dollars.
# Explanation
#
# Given:
# , ,
#
# Calculations:
#
# We
# round
# to
# the
# nearest
# dollar(integer) and then
# print
# our
# result:
#
# The
# total
# meal
# cost is 15
# dollars.

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * (tip_percent/100)
    tax = meal_cost * (tax_percent/100)
    total_cost = meal_cost + tip + tax
    print("The total meal cost is", round(meal_cost + tip + tax),"dollars.")
    return


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)