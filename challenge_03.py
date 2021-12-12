import sys
from collections import Counter


def parse_input():
    return list(map(lambda x: x.split(":"), sys.stdin.readlines()))


def solve(inpt):
    non_corrupt = 0
    for a, passwd in inpt:
        reg, letter = a.split()
        minimum, maximum = tuple(map(int, reg.split("-")))
        cnt = Counter(passwd).get(letter, 0)
        if minimum <= cnt <= maximum:
            non_corrupt += 1
    return non_corrupt


def main():
    inpt = parse_input()
    solution = solve(inpt)
    print(solution)


if __name__ == "__main__":
    main()
