# 10 Days of Statistics: Day 1: Standard Deviation


def calc_median(inputs):
    size = len(inputs)
    inputs.sort()
    if size % 2 == 0:
        # Even
        median = (inputs[int(size/2) - 1] + inputs[int(size/2)])/2
    else:
        # Odd
        median = inputs[int(size/2)]

    return median


def create_list(inputs, freq):
    data = []
    for i in range(len(inputs)):
        data += [inputs[i]]*freq[i]
    data.sort()
    return data


if __name__ == "__main__":
    n = int(input())
    inputs = list(map(int, input().split()))
    freq = list(map(int, input().split()))
    data = create_list(inputs, freq)

    Q2 = calc_median(data)
    size = len(data)
    Q1 = calc_median(data[0:size//2])
    if size % 2 == 0:
        # Even
        Q3 = calc_median(data[size//2:])
    else:
        # Odd
        Q3 = calc_median(data[size//2 + 1:])
    print(float(Q3-Q1))