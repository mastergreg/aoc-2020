import sys


def parse_input():
    return list(map(int, sys.stdin.readlines()))


def solve(inpt):
    print(len(inpt))
    for x in inpt:
        for y in inpt:
            z = 2020 - x - y
            if z in inpt:
                return x * y * z


def main():
    inpt = parse_input()
    solution = solve(inpt)
    print(solution)


if __name__ == "__main__":
    main()
