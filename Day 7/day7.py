import re
from collections import deque

# get bags with content-> "color 1": {"color 2":1, "color 3": 5}
# I don't know what these values are for, but I'm sure they'll come in handy


def get_bags(lines):
    # initialize an empty dict
    bags = dict()
    for line in lines:
        # remove all commas, dots and bag/bags words
        colors = re.sub(r",|\.|bag[s]?", '', line)
        # split by contain, we get ["parent", "children"]
        [parent, children] = re.split("  contain ", colors)
        # split children by double spaces (we removed commas and we're left with double spaces between entries)
        children = re.split("  ", children)
        for child in children:
            # if theres no entry for that color, add one
            if not parent in bags:
                bags[parent] = {}
            if child != "no other ":
                # if there is another bag, add it as a child
                bags[parent].update({child[2:].rstrip(): int(child[0])})
    return(bags)


def get_indexes(bags):
    # I wanted to make a bidirectional dict/map, i guess I could just use generated objects but that really simplified the proccess
    index_dict = {}
    index = 0
    for bag in bags:
        # index each bag by number
        index_dict[index] = bag
        index += 1
    # reverse each (key, value) tuple in dict, and make another dict out of it
    rev_dict = dict([reversed(item) for item in index_dict.items()])
    # add reversed tuples to the output
    index_dict.update(rev_dict)
    # index_dict -> {1:"abc", "abc":1, ...}
    return(index_dict)


def make_graph(indexes, bags):
    # make graph in the form of tuples (from_index, to_index)
    graph = []
    for bag in bags:
        for child in bags[bag]:
            graph.append((indexes[bag], indexes[child]))
    return graph


def make_adj_matrix(graph, N):
    # prepare adjacency matrix: a list of nodes reachable from each node
    adj_list = [[] for _ in range(N)]
    for (fr, to) in graph:
        adj_list[fr].append(to)
    return adj_list


def find_path(adj_matrix, fr, to, discovered):
    # BFS traversal
    # example graph: (0,1), (0,2), (1,3), (2,3), (3,4)
    # we look for the 0-3 path. We mark 0 as visited put it in the queue. We pop it from the queue, check 1 and 2, they both aren't
    # visited, so we mark these as visited and append them to our queue. We pop 1 - it isn't our goal. We mark 3 as visited and append
    # it to the queue, because it wasn't visited yet. We pop 2 from the queue. It isn't our goal either. We check for nodes available from 2.
    # 3 is visited, so we don't append anything to our queue. We pop 3 from the queue, it isn't our goal. We append 4 to the queue, mark it
    # as visited, and we pop it from the queue right after. It is our goal, so we return True.

    # initialize a FIFO queue
    q = deque()
    # mark fr (from) as visited
    discovered[fr] = True
    # add the starting node to the queue
    q.append(fr)
    # while theres something in the queue
    while(q):
        # pop the oldest element
        node = q.popleft()
        # if the element is the searched node, return true
        if node == to:
            return True
        # if it isn't the goal and we didn't visit it yet, add it to the queue and mark as visited
        for available in adj_matrix[node]:
            if not discovered[available]:
                discovered[available] = True
                q.append(available)
    # if there's nothing else in the queue and you didn't find the goal, there's no path from starting node to the destination
    return False

# recursive function couting bags in a bag


def get_bags_rec(name, bags):
    # get bags contained in a bag
    sub_bags = bags[name].items()
    sum = 0
    if sub_bags:
        for bag in sub_bags:
            # sum bags themselves and all the bags contained in them recursively
            sum += bag[1] + bag[1] * get_bags_rec(bag[0], bags)
    else:
        # if theres no bags inside, return 0
        return 0
    return sum


def part_1(lines):
    bags = get_bags(lines)
    node_count = len(bags)
    indexes = get_indexes(bags)
    graph = make_graph(indexes, bags)
    adj_matrix = make_adj_matrix(graph, node_count)
    connected = 0
    # we look for bags that include shiny gold bags
    to = "shiny gold"
    for bag in bags:
        discovered = [False]*node_count
        if bag != to:
            if find_path(adj_matrix, indexes[bag], indexes[to], discovered):
                connected += 1
    return connected


def part_2(lines):
    bags = get_bags(lines)
    bag = "shiny gold"
    return get_bags_rec(bag, bags)


input_file = open("input.txt", 'r')
lines = input_file.read().splitlines()
print("PART 1: ", part_1(lines))
print("PART 2: ", part_2(lines))
