import sys
import re


def parse_input():

    data = sys.stdin.read()
    passports = []
    for passport in data.split("\n\n"):
        fields = list(map(lambda x: tuple(x.split(":")), passport.split()))
        passports.append(dict(fields))

    return passports


def check_byr(byr):
    return 1920 <= int(byr) <= 2002


def check_iyr(iyr):
    return 2010 <= int(iyr) <= 2020


def check_eyr(eyr):
    return 2020 <= int(eyr) <= 2030


def check_hgt(hgt: str):
    if hgt.endswith("cm"):
        return 150 <= int(hgt[:-2]) <= 193
    if hgt.endswith("in"):
        return 59 <= int(hgt[:-2]) <= 76
    return False


def check_hcl(hcl: str):
    regex = r"#[0-9a-f]"
    return re.match(regex, hcl) is not None


def check_ecl(ecl: str):
    valid_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return ecl in valid_ecl


def check_pid(pid: str):
    return pid.isdigit() and len(pid) == 9


def check_passport(passport):
    CHECK_MAP = {
        "byr": check_byr,
        "iyr": check_iyr,
        "eyr": check_eyr,
        "hgt": check_hgt,
        "hcl": check_hcl,
        "ecl": check_ecl,
        "pid": check_pid,
    }
    for field in CHECK_MAP.keys():
        yield field in passport and CHECK_MAP[field](passport[field])


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
