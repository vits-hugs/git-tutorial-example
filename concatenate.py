def concatenate_all(strings: list[int]) -> int:
    return "".join(strings)

if __name__ == '__main__':
    import sys
    print(concatenate_all(sys.argv[1:]))
