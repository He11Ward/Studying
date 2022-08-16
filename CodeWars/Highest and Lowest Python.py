def high_and_low(numbers):
    return rf"{max([int(x) for x in numbers.split()])} {min([int(x) for x in numbers.split()])}"
