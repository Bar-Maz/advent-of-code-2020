from copy import deepcopy

def parse_instruction(str):
    # each instruction looks like: ins +4
    tokens = str.split(' ')
    # we need to keep track of the visited instructions to prevent loops
    return {
        "op": tokens[0],
        "val": int(tokens[1]),
        "visited": False
    }


def get_instructions(lines):
    # get all instructions from a file
    return [parse_instruction(line) for line in lines]


def get_all_nop_jmp(instructions):
    # get all nop and jmp instructions from a file
    return [{"ins": instr, "idx": idx} for idx, instr in enumerate(instructions) if instr["op"] in ["jmp", "nop"]]


def part_1(lines):
    instructions = get_instructions(lines)
    # initialize index and accumulator with 0
    index = 0
    acc = 0
    while True:
        instr = instructions[index]
        # get op and val from instruction dictionary
        # we can get visited because it wouldn't get modified in the array
        (op, val) = (instr["op"], instr["val"])
        # terminate the program
        if(instr["visited"]):
            return acc
        # mark current instruction as visited
        instr["visited"] = True
        # don't do anything if it's a nop instruction
        if(op != "nop"):
            # if it's jump, modify current index and continue to another loop iteration
            if(op == "jmp"):
                index += val
                continue
            # if it's neither jmp or nop, it has to be acc
            else:
                acc += val
        # increment index after nops and accs (jmp continues the loop)
        index += 1


def part_2(lines):
    instructions = get_instructions(lines)
    jmp_nop = get_all_nop_jmp(instructions)
    # just bruteforcing it, I don't really have an idea on how to optimize it
    for jn in jmp_nop:
        # need to deep copy, because objects were getting modified in both arrays
        new_instructions = deepcopy(instructions)
        #swap one jmp or nop instruction
        new_instructions[jn["idx"]]["op"] = "nop" if jn["ins"]["op"] == "jmp" else "nop"
        index = 0
        acc = 0
        # check max index 
        max_index = len(new_instructions) - 1
        while True:
            if(index > max_index):
                # program should terminate after trying to execute an instruction immediately after the last instruction in the file
                if(index == max_index + 1):
                    return acc
                # if program tries to jump to an index higher than one after the last instruction in the file
                # just print it's index (didn't happen with this input though)
                else:
                    print("IndexError: " + str(index))
            instr = new_instructions[index]
            # we return the value under a different condition earlier, just break here
            if(instr["visited"]):
                break
            instr["visited"] = True
            (op, val) = (instr["op"], instr["val"])
            if(op != "nop"):
                if(op == "jmp"):
                    index += val
                    continue
                else:
                    acc += val
            index += 1


input_file = open("input.txt", 'r')
lines = input_file.read().splitlines()
print("PART 1: ", part_1(lines))
print("PART 2: ", part_2(lines))
