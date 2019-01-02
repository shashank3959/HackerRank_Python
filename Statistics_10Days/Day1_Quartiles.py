# 10 Days of Statistics: Day 1: Quartiles


def calc_median(inputs):
    size = len(inputs)
    inputs.sort()
    if size % 2 == 0:
        # Even
        median = int((inputs[int(size/2) - 1] + inputs[int(size/2)])/2)
    else:
        # Odd
        median = inputs[int(size/2)]

    return median


if __name__ == "__main__":
    n = int(input(""))
    inputs = list(map(int, input().split()))
    Q2 = calc_median(inputs)
    size = len(inputs)
    Q1 = calc_median(inputs[0:size//2])
    if size % 2 == 0:
        # Even
        Q3 = calc_median(inputs[size//2:])
    else:
        # Odd
        Q3 = calc_median(inputs[size//2 + 1:])

    print(Q1)
    print(Q2)
    print(Q3)

