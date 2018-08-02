# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem


from collections import defaultdict

n, m = input().split()
dict_a = defaultdict(list)
for i in range(int(n)):
    dict_a[input()].append(str(i+1))

for i in range(int(m)):
    inp = input()
    string = " ".join(dict_a[inp])
    if len(string) != 0:
        print(string)
    else:
        print("-1")
