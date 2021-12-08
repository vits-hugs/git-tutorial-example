def accumulate(numbers: list[int]) -> int:
    result = 0
    for n in numbers:
        result += n
    return result

if __name__ == '__main__':
    import sys
    numbers = [int(arg) for arg in sys.argv[1:]]
    print(accumulate(numbers))
