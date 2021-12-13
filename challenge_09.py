import sys
import re


def parse_input():
    data = map(lambda x: x.strip(), sys.stdin.readlines())
    bpasses = list(map(lambda x: (x[:7], x[7:]), data))
    return bpasses


def solve(inpt):
    valid = 0
    return inpt


def main():
    inpt = parse_input()
    solution = solve(inpt)
    print(solution)


if __name__ == "__main__":
    main()
