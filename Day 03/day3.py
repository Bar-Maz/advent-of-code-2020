from functools import reduce


def count_trees(input_file, slopes):
    # we need line length to wrap around the input
    line_length = len(input_file.readline().strip('\n'))
    # array of current line indexes for each slope
    indexes = [0]*len(slopes)
    # array of numbers of trees for each slope
    values = [0]*len(slopes)
    # we iterate over the file without the 1st line, because we've already read it while calculating line_length
    for line_idx, line in enumerate(input_file.read().splitlines()):
        # we iterate over the slopes r - step right, d - step down
        for idx, (r, d) in enumerate(slopes):
            # we subtract one because we've started for the second line, if the step > 1, we need to check it only every <d>nd/rd/th line
            if (line_idx-1) % d == 0:
                # new index increased by step right value
                new_index = (indexes[idx] + r) % line_length
                indexes[idx] = new_index
                # if the character under the current index is a tree, we increment tree count for the current slope
                values[idx] += line[new_index] == '#'
    return(reduce(lambda x, y: x*y, values))


def part_1(input_file):
    return count_trees(input_file, [(3, 1)])


def part_2(input_file):
    return count_trees(input_file, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])


with open("input.txt", 'r') as input_file:
    print("PART 1: ", part_1(input_file))
with open("input.txt", 'r') as input_file:
    print("PART 2: ", part_2(input_file))
