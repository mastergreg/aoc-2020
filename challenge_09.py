import sys
import re
import math


def parse_input():
    data = map(lambda x: x.strip(), sys.stdin.readlines())
    bpasses = list(map(lambda x: (x[:7], x[7:]), data))
    return bpasses

def bsearch_row(row_code):
    mn = 0
    mx = 127
    for c in row_code:
        if c == "F":
            mx = math.floor((mn + mx) / 2)
        if c == "B":
            mn = math.ceil((mn + mx) / 2)
    return mn

def bsearch_col(col_code):
    mn = 0
    mx = 7
    for c in col_code:
        if c == "L":
            mx = math.floor((mn + mx) / 2)
        if c == "R":
            mn = math.ceil((mn + mx) / 2)
    return mn

def calc_seat_id(inpt):
    a, b = inpt
    row = bsearch_row(a)
    col = bsearch_col(b)
    return row * 8 + col


def solve(inpt):
    mx = 0
    for bpass in inpt:
        mx = max(calc_seat_id(bpass), mx)
    return mx


def main():
    inpt = parse_input()
    solution = solve(inpt)
    print(solution)


if __name__ == "__main__":
    main()
