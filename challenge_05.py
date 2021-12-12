import sys
from collections import Counter


def parse_input():
    return list(map(lambda x: x.strip(), sys.stdin.readlines()))


def nxt(a, b):
    return lambda i, j: (i + a, j + b)


def nxt_3_1(i, j):
    return i + 3, j + 1


def traverse(inpt, nxt):
    width = len(inpt[0])
    i = 0
    j = 0
    i, j = nxt(i, j)
    while j < len(inpt):
        yield inpt[j][i % width]
        i, j = nxt(i, j)


def solve_a_b(inpt, a, b):
    trees = 0
    for pos in traverse(inpt, nxt(a, b)):
        if pos == "#":
            trees += 1
    return trees


def solve(inpt):
    routes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    tree_list = [solve_a_b(inpt, a, b) for a, b in routes]
    result = 1

    for tree_count in tree_list:
        result *= tree_count
    return result


def main():
    inpt = parse_input()
    solution = solve(inpt)
    print(solution)


if __name__ == "__main__":
    main()
