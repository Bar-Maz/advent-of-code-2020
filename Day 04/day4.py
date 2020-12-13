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


def get_correct_entries(entries):
    # we return the list of dicts which sets of keys contain all of the required fields
    return [x for x in entries if set(x.keys()).issuperset({"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"})]


def check_entry(e):
    # check if byr, iyr and eyr are in the correct range
    if int(e["byr"]) < 1920 or int(e["byr"]) > 2002:
        return False
    if int(e["iyr"]) < 2010 or int(e["iyr"]) > 2020:
        return False
    if int(e["eyr"]) < 2020 or int(e["eyr"]) > 2030:
        return False
    # get only letters for hgt - replace all numbers(\d) with empty strings
    unit = re.sub('\d', '', e["hgt"])
    # check if unit is cm or in
    if unit not in ["cm", "in"]:
        return False
    # find all numbers in hgt, if you found 0 or more than 1 ("11asd12" will return ['11', '12']) discard the entry
    numbers = re.findall(r'\d+', e["hgt"])
    if len(numbers) != 1:
        return False
    # convert the one found number string to int
    height = int(numbers[0])
    # check if height is in the correct range
    if unit == "cm" and (height < 150 or height > 193):
        return False
    if unit == "in" and (height < 59 or height > 76):
        return False
    # check if hcl has correct format
    # ^ - beginning of a string
    # # - just a # character
    # [0-9a-f]{6} - 6 characters from 0 to 9 or from a to f
    # $ - end of a string
    if not re.match("^#[0-9a-f]{6}$", e["hcl"]):
        return False
    # check if ecl has one of the allowed values
    # ^ - beginning of a string
    # # - just a # character
    # [0-9a-f]{6} - 6 characters from 0 to 9 or from a to f
    # $ - end of a string
    if e["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
    # check if pid is a string with 9 digits
    if not re.match("^[0-9]{9}$", e["pid"]):
        return False
    # if you didn't return False, this entry is correct
    return True


def part_1(lines):
    entries = parse_passports(lines)
    correct_entries = get_correct_entries(entries)
    return len(correct_entries)


def part_2(lines):
    entries = parse_passports(lines)
    correct_entries = get_correct_entries(entries)
    return sum([check_entry(e) for e in correct_entries])


input_file = open("input.txt", 'r')
lines = input_file.readlines()
print("PART 1: ", part_1(lines))
input_file = open("input.txt", 'r')
lines = input_file.readlines()
print("PART 2: ", part_2(lines))
