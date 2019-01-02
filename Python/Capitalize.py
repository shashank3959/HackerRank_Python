# You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.
#
#
# Given a full name, your task is to capitalize the name appropriately.
#
# Input Format
#
# A single line of input containing the full name, .
#
# Constraints
#
# The string consists of alphanumeric characters and spaces.
# Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.
#
# Output Format
#
# Print the capitalized string, .
#
# Sample Input
#
# chris alan
# Sample Output
#
# Chris Alan


def fix(string):
    string = list(string)
    if len(string) == 0:
        return ""

    c = 0
    while string[c] == ' ':
        c += 1

    if string[c].islower():
        string[c] = string[c].upper()
    string = "".join(string)
    return string


def solve(string):
    string = string.split(" ")
    print(string)
    string = [fix(string[i]) for i in range(len(string)) if string != '']
    string = " ".join(string)
    return string


if __name__ == '__main__':
    s = input()
    print(solve(s))

