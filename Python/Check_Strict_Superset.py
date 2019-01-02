# You are given a set  and  other sets.
# Your job is to find whether set  is a strict superset of each of the  sets.

# Print True, if  is a strict superset of each of the  sets. Otherwise, print False.

# A strict superset has at least one element that does not exist in its subset.

# Example
# Set is a strict superset of set.
# Set is not a strict superset of set.
# Set is not a strict superset of set.

# Input Format

# The first line contains the space separated elements of set .
# The second line contains integer , the number of other sets.
# The next  lines contains the space separated elements of the other sets.

# Constraints

# Output Format

# Print True if set  is a strict superset of all other  sets. Otherwise, print False.

# Sample Input 0

# 1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
# 2
# 1 2 3 4 5
# 100 11 12
# Sample Output 0

# False
# Explanation 0

# Set  is the strict superset of the set but not of the set because  is not in set .
# Hence, the output is False.

if __name__ == "__main__":
    setA = set(map(int, input().split()))
    n = int(input())
    flag = 0
    for i in range(n):
        setB = set(map(int, input().split()))
        if len(setA) != len(setB):
            if setA.issuperset(setB) != True:
                flag = 1

    if flag == 0:
        print("True")
    else:
        print("False")