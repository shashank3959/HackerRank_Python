# https://www.hackerrank.com/challenges/30-scope/problem

class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self):
        absol = 0
        self.maximumDifference = 0
        for i in range(len(self.__elements)):
            for j in range(i, len(self.__elements)):
                absol = abs(self.__elements[i] - self.__elements[j])
                if absol > self.maximumDifference:
                    self.maximumDifference = absol

    # End of Difference class


if __name__ == "__main__":
    _ = input()
    a = [int(e) for e in input().split(' ')]

    d = Difference(a)
    d.computeDifference()

    print(d.maximumDifference)
