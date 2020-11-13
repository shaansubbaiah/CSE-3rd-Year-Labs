class Node:
    def __init__(self, state, level):
        self.grid = state
        self.level = level
        self.cost = 0


# Using g(x) = current level
def G(state):
    return state.level


# using h(x) = manhattan distance = sum of distances required by each tile in the puzzle
def H(state, target):
    grid = state.grid

    dist = 0
    for i in grid:
        d1, d2 = grid.index(i), target.index(i)
        x1, y1 = d1 % 3, d1 // 3
        x2, y2 = d2 % 3, d2 // 3
        # sum the distances
        dist += abs(x1 - x2) + abs(y1 - y2)

    return dist


# calculate A* = g(x) + h(x)
def F(state, target):
    return G(state) + H(state, target)


# display the puzzle
def printGrid(state):
    state = state.grid.copy()
    state[state.index(-1)] = " "
    print(state[0], state[1], state[2])
    print(state[3], state[4], state[5])
    print(state[6], state[7], state[8])
    print()


def inFrontier(frontier, neighbour):
    return len([state for state in frontier if state.grid == neighbour.grid]) > 0


# main A* function
def astar(state, target):
    frontier = [Node(state, 1)]

    while frontier:
        frontier.sort(key=lambda x: x.cost)
        state = frontier.pop(0)
        print(f"Level: {state.level}")
        printGrid(state)

        if state.level >= 4:
            print(f"NOTFOUND")
            return

        if state.grid == target:
            print(f"Success!!!")
            return

        neighbours = possible_moves(state)
        for neighbour in neighbours:
            neighbour = Node(neighbour, state.level + 1)
            neighbour.cost = F(neighbour, target)
            if not inFrontier(frontier, neighbour):
                frontier.append(neighbour)

    print("Fail!!!")


# define possible moves for each position in the puzzle
def possible_moves(state):
    b = state.grid.index(-1)
    d = []
    if b not in [0, 1, 2]:
        d += "u"
    if b not in [6, 7, 8]:
        d += "d"
    if b not in [2, 5, 8]:
        d += "r"
    if b not in [0, 3, 6]:
        d += "l"
    pos_moves = []
    for move in d:
        pos_moves.append(gen(state, move, b))
    return pos_moves


# generate the nodes based on possible moves
def gen(state, move, blank):
    temp = state.grid.copy()
    if move == "u":
        temp[blank - 3], temp[blank] = temp[blank], temp[blank - 3]
    if move == "d":
        temp[blank + 3], temp[blank] = temp[blank], temp[blank + 3]
    if move == "r":
        temp[blank + 1], temp[blank] = temp[blank], temp[blank + 1]
    if move == "l":
        temp[blank - 1], temp[blank] = temp[blank], temp[blank - 1]
    return temp


# input source puzzle
print("Enter src:")
src = list(map(int, input().split(" ")[:9]))

# define the target puzzle
target = [1, 2, 3, 4, 5, 6, 7, 8, -1]

# start the program
astar(src, target)