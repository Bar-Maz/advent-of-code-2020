def part_1(input_file):
    line_length = len(input_file.readline().strip('\n'))
    index = 0
    tree_count = 0
    for line in input_file.read().splitlines():
        index += 3
        tree_count += line[index % line_length] == '#'
    return(tree_count)


input_file = open("input.txt", 'r')
print("PART 1: ", part_1(input_file))
