import re

# apply the mask: replace 0 with 0 and  1 with 1, copy the characters at X positions


def apply_mask(value, mask):
    val = bin(int(value))[2:]
    # add leading zeros
    val = "0" * (len(mask) - len(val)) + val
    val = "".join([char if not char == 'X' else val[idx]
                   for idx, char in enumerate(mask)])
    return val


def get_mask_values(mask):
    # initialize options
    options = []
    # here X means 0 or 1, 1 means 1 and 0 means copy
    # made it compatible with function used it part 1
    for idx, char in enumerate(mask):
        if char == 'X':
            options.append(['0', '1'])
        elif char == '1':
            options.append(['1'])
        else:
            options.append(['X'])
    values = [""]
    # construct character by character each possible mask
    for op in options:
        current_values = []
        for letter in op:
            for value in values:
                current_values.append(value + letter)
        values = current_values
    return values


def part_1(lines):
    mem = {}
    mask = ""
    for line in lines:
        # check if current line includes a mask
        if line[:4] == "mask":
            mask = line[7:]
        else:
            # delete unnecessary characters, split by '='
            addr, value = re.split(" = ", re.sub("mem|\[|\]", "", line))
            # get value with a mask
            binary = apply_mask(value, mask)
            # save it to memory
            mem[int(addr)] = int(binary, 2)
    return sum([mem[addr] for addr in mem])


def part_2(lines):
    mem = {}
    mask = ""
    for line in lines:
        if line[:4] == "mask":
            mask = line[7:]
        else:
            addr, value = re.split(" = ", re.sub("mem|\[|\]", "", line))
            # get all possible masks
            mask_values = get_mask_values(mask)
            # apply each mask and save to each memory address
            for new_mask in mask_values:
                masked_addr = apply_mask(addr, new_mask)
                mem[int(masked_addr, 2)] = int(value)
    return sum([mem[addr] for addr in mem])


input_file = open("input.txt", 'r')
lines = input_file.read().splitlines()
print("PART 1: ", part_1(lines))
print("PART 2: ", part_2(lines))
