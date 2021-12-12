import sys
from collections import Counter


def parse_input():
    return sys.stdin.readlines()


def next(i, j):
    return i + 3, j + 1


def traverse(inpt):
    i = 0
    j = 0
    while j < len(inpt):
        i, j = next(i, j)
        yield inpt[i][j]


def solve(inpt):
    trees = 1
    for pos in traverse(inpt):
        if pos == "#":
            trees += 1
    return trees


def main():
    inpt = parse_input()
    solution = solve(inpt)
    print(solution)


if __name__ == "__main__":
    main()
