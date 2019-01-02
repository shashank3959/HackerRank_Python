# 10 Days of Statistics: Day 0: Mean, Median and Mode


def mean_calc(inputs):
    return sum(inputs)/len(inputs)


def median_calc(inputs):
    inputs.sort()
    length = len(inputs)
    if length % 2 == 0:
        return (inputs[int(length/2-1)] + inputs[int(length/2)])/2


# we will maintain a dictionary of elements and their counts
def mode_calc(inputs):
    mydict = dict()
    maxels = []  # List of mode elements
    max = float("-inf")  # Definition of the max element

    for i in inputs:
        if i in mydict:
            mydict[i] += 1
        else:
            mydict[i] = 1

    for j in mydict:
        if mydict[j] > max:
            del maxels
            maxels = []
            maxels.append(j)
            print("Appending element:", j, mydict[j])
            max = mydict[j]

        elif mydict[j] == max:
            maxels.append(j)
            print("Check for :", mydict[j])

    return min(maxels)


if __name__ == "__main__":
    n=int(input("Enter the number of inputs:"))
    inputs = list(map(int, input("Enter the numbers:").split()))

    # Print the mean
    print(mean_calc(inputs))
    print(median_calc(inputs))
    print(mode_calc(inputs))

