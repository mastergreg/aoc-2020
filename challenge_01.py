import sys


def parse_input():
    return list(map(int, sys.stdin.readlines()))


def solve(inpt):
    print(len(inpt))
    for x in inpt:
        y = 2020 - x
        if y in inpt:
            return x * y


def main():
    inpt = parse_input()
    solution = solve(inpt)
    print(solution)


if __name__ == "__main__":
    main()
