# You are given a string  and width .
# Your task is to wrap the string into a paragraph of width .
#
# Input Format
#
# The first line contains a string, .
# The second line contains the width, .
#
# Constraints
#
# Output Format
#
# Print the text wrapped paragraph.
#
# Sample Input 0
#
# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
# Sample Output 0
#
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

def wrap(string, max_width):
    string = list(string)
    wrapped_string = []
    for i in range(len(string)):
        if i % max_width == 0 and i > 0:
            wrapped_string.append('\n')
        wrapped_string.append(string[i])
    string = ''.join(wrapped_string)

    return string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
