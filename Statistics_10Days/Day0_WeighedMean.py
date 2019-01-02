# 10 Days of Statistics: Day 0: Weighed Mean

def calc_weighted_mean(ints, weights):
    if len(ints) != len(weights):
        print("Error: number of integers different from the number of weights!")

    weighted_sum = sum([a*b for a,b in zip(ints, weights)])
    return weighted_sum/sum(weights)


if __name__ == "__main__":
    n = int(input(""))
    input_ints = list(map(int, input("").split()))
    input_weights = list(map(int, input("").split()))
    print("{:.1f}".format(calc_weighted_mean(input_ints, input_weights)))
