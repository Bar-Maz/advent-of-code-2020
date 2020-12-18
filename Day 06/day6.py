def part1(lines):
    answers_set = set({})
    answers_sum = 0
    for line in lines:
        if line:
            # if we convert a string to a set, we get a set with all letters in a string
            # example: set("banana") -> {'b', 'a', 'n'}
            # set1 | set2 returns union of two sets: answers given in either line
            # {'b', 'a', 'n'} | {'n', 'o', 't'} -> {'b', 'a', 'n', 'o', 't'}
            answers_set |= set(line)
        else:
            # empty line == end of the group, we count how many answers did we get and add these to our sum
            answers_sum += len(answers_set)
            answers_set = set({})
    # no empty line at the end of the input
    answers_sum += len(answers_set)
    return answers_sum


def part2(lines):
    answers_set = set({})
    answers_sum = 0
    # flag indicating if current line is first in the group, because intersecting anything with an empty set gives us an empty set
    is_first = True
    for line in lines:
        if line:
            if is_first:
                # if it's the first line in the group, set it as answers_set, then we'll intersect all the other sets with this
                answers_set = set(line)
                # we already have a first set, so other lines are not 1st anymore
                is_first = False
            else:
                # set1.intersect(set2) returns intersection of two sets: answers given in both lines
                # {'b', 'a', 'n'} | {'n', 'o', 't'} -> {'n'}
                answers_set = answers_set.intersection(set(line))
        else:
            # next line read will be 1st in its group
            is_first = True
            answers_sum += len(answers_set)
            answers_set = set({})
    # no empty line at the end of the input
    answers_sum += len(answers_set)
    return answers_sum

with open("input.txt", 'r') as input_file:
    lines = input_file.read().splitlines()
    print("PART 1: ", part1(lines))
    print("PART 2: ", part2(lines))
