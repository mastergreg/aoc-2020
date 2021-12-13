import sys
import re


def parse_input():

    data = sys.stdin.read()
    passports = []
    for passport in data.split("\n\n"):
        fields = list(map(lambda x: tuple(x.split(":")), passport.split()))
        passports.append(dict(fields))

    return passports


def check_passport(passport):
    MANDATORY = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    for field in MANDATORY:
        yield field in passport


def solve(inpt):
    valid = 0
    for passport in inpt:
        if all(check_passport(passport)):
            valid += 1
    return valid


def main():
    inpt = parse_input()
    solution = solve(inpt)
    print(solution)


if __name__ == "__main__":
    main()
