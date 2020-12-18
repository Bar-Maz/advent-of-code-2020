import re
from itertools import tee


def convert_to_binary(seat):
    # replace B and R (upper halves) with 1 and F and L (lower halves) with 0, then convert it to a base 2 integer
    return int(re.sub(r"[BR]", "1", re.sub(r"[FL]", "0", seat)), 2)


def get_pairs(list):
    # tee returns two iterators based on a iterable
    a, b = tee(list)
    # skip the first element of the second iterator
    next(b)
    # zip returns an array of tuples based on given iterables
    # this array looks like this: [(list[0], list[1]), (list[1], list[2]) ...]
    return zip(a, b)

# get max seat number from all the given seats encoded with F, B, L, R


def part1(lines):
    max = 0
    for seat in lines:
        seat_nr = convert_to_binary(seat)
        if seat_nr > max:
            max = seat_nr
    return max

# sort all seats, get pairs of them and search for a free seat


def part2(lines):
    for pair in get_pairs(sorted([convert_to_binary(seat) for seat in lines])):
        if pair[0] + 1 != pair[1]:
            return pair[0] + 1
    return None


with open("input.txt", 'r') as input_file:
    lines = input_file.readlines()
    print("PART 1: ", part1(lines))
    print("PART 2: ", part2(lines))
