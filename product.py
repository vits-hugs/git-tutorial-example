from functools import reduce
from operator import mul


def multiply_all(numbers: list[int]) -> int:
    return reduce(mul, numbers, 1)

if __name__ == '__main__':
    import sys
    numbers = [int(arg) for arg in sys.argv[1:]]
    print(multiply_all(numbers))
