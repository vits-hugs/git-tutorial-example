def concatenate(strings: list[int]) -> int:
    return "".join(strings)

if __name__ == '__main__':
    import sys
    print(concatenate(sys.argv[1:]))
