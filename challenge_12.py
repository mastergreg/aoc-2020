import sys
import re
import math


def parse_input(file_inpt=sys.stdin):
    data = list(map(lambda x: x.split(), file_inpt.read().split("\n\n")))
    return data

def count_unique_letters(group):
    letters = set()
    for letter in "".join(group):
        letters.add(letter)
    return len(letters)

def count_common_letters(group):
    return len(set.intersection(*list(map(set, group))))

def solve(inpt):
    return sum(map(count_common_letters, inpt))

def main():
    inpt = parse_input()
    solution = solve(inpt)
    print(solution)


if __name__ == "__main__":
    main()
