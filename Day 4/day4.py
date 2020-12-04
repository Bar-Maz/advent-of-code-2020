import re


def parse_passports(lines):
    entry = ""
    entries = []
    # we split each entry by whitespaces(\s+), and then we construct dicts using read values

    def add_entry(entry):
        entries.append({x and re.split(":", x)[0]: re.split(":", x)[1]
                        for x in re.split("\s+", entry) if x})
    # entries are separated by empty lines
    for line in lines:
        if line == "\n":
            add_entry(entry)
            entry = ""
        else:
            entry += line
    # last entry isn't followed by a newline
    add_entry(entry)
    return entries


def part_1(lines):
    entries = parse_passports(lines)
    # we check if set of keys in our dict contains all of the required fields and then we sum all the outputs together
    return sum([set(x.keys()).issuperset({"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}) for x in entries])


input_file = open("input.txt", 'r')
lines = input_file.readlines()
print("PART 1: ", part_1(lines))
