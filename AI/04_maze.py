import math

maze = []
path = []
closedPath = []
neigbhours = [[1, 1], [0, 1], [1, 0], [1, -1], [0, -1], [-1, 1], [-1, 0], [-1, -1]]


def euclidDist(x, dest):
    dist = math.sqrt((dest[0] - x[0]) ** 2 + (dest[1] - x[1]) ** 2)
    return dist


def findShortestPath(nextPath, dest):
    minDistance = 999
    next = []
    for x in nextPath:
        if euclidDist(x, dest) < minDistance:
            minDistance = euclidDist(x, dest)
            next = x

    return next


def findPath(n, m, start, dest):
    path.append(start)

    current = start

    while current != dest:
        nextPath = []
        for x in neigbhours:
            a = []
            a.append(current[0] + x[0])
            a.append(current[1] + x[1])
            if a[0] > -1 and a[0] < n and a[1] > -1 and a[1] < m:
                if maze[a[0]][a[1]]:
                    if a not in path and a not in closedPath:
                        nextPath.append(a)

        if nextPath:
            current = findShortestPath(nextPath, dest)
            path.append(current)
        else:
            if path:
                closedPath.append(current)
                path.pop()
                if path:
                    current = path[len(path) - 1]
                else:
                    print("NO PATH")
                    exit(0)
            else:
                print("NO PATH")
                exit(0)


def start():
    n = int(input("\nEnter number of rows: "))
    m = int(input("\nEnter number of cols: "))

    print("\nEnter the maze structure: (0-blocked,1-free): ")

    for i in range(n):
        a = []
        # for j in range(m):
        #     a.append(int(input()))
        a = list(map(int, input().split(" ")))
        maze.append(a)

    print("Enter start position: ", end="")
    start = []
    start = list(map(int, input().split(" ")))

    print("Enter destination position: ", end="")
    dest = []
    dest = list(map(int, input().split(" ")))

    print("\n\n***MAZE***")
    for i in range(n):
        for j in range(m):
            print(maze[i][j], end=" ")
        print()

    findPath(n, m, start, dest)

    print("\n**PATH**")
    for i in range(n):
        for j in range(m):
            if [i, j] in path:
                print("-", end=" ")
            else:
                print(maze[i][j], end=" ")
        print()

    print()
    print(path)


if __name__ == "__main__":
    start()