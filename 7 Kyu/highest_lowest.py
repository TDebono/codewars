def high_and_low(numbers):
    n = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(n),min(n))