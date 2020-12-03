from functools import reduce


def count_trees(input_file, slopes):
    line_length = len(input_file.readline().strip('\n'))
    indexes = [0]*len(slopes)
    values = [0]*len(slopes)
    for line_idx, line in enumerate(input_file.read().splitlines()):
        for idx, (r, d) in enumerate(slopes):
            if (line_idx-1) % d == 0:
                new_index = (indexes[idx] + r) % line_length
                indexes[idx] = new_index
                values[idx] += line[new_index] == '#'
    print([indexes, values])
    return(reduce(lambda x, y: x*y, values))


def part_1(input_file):
    return count_trees(input_file, [(3, 1)])


def part_2(input_file):
    return count_trees(input_file, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])


input_file = open("input.txt", 'r')
print("PART 1: ", part_1(input_file))
input_file = open("input.txt", 'r')
print("PART 2: ", part_2(input_file))
