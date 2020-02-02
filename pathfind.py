import queue


def createMaze():
    maze = []
    maze.append(["#", "#", "#", "#", "#", "O", "#"])
    maze.append(["#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", "#", "#", " ", "#"])
    maze.append(["#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", "#", "#", "X", "#", "#", "#"])

    return maze


def print_maze(maze):  # function to print the maze as it is
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            print(maze[i][j], end="")
            print(" ", end="")
        print()


def find_starting_pos(maze):  # function to find the starting postion of the maze
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "O":
                return i, j  # returns the pos coordinates as col, row (y,x)


our_queue = ""
our_maze = createMaze()
print_maze(our_maze)
print(find_starting_pos(our_maze))
