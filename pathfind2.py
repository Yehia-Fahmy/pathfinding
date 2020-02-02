import queue


def createSmallMaze():
    maze = []
    maze.append([" ", " ", "O"])
    maze.append([" ", " ", " "])
    maze.append(["X", " ", " "])

    return maze


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


def queue_test():
    queue1 = [" ", " "]
    x = queue1.pop(0)
    while len(x) < 5:
        x = queue1.pop(0)
        queue1.append(x + "R")
        queue1.append(x + "L")
        queue1.append(x + "D")
        queue1.append(x + "U")
    print(len(x))
    print(queue1)


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


def add_valid(
    starting_pos, queue
):  # this function will add any valid paths to the queue
    current_pos = (
        starting_pos
    )  # using the starting position as a start we follow the path at the top of the queue to find the current position
    path = queue.pop(0)
    temp = (
        path
    )  # we dont want to modify the path we are dealing with so we use a temp for the next step
    while len(temp) > 0:
        next_move = temp.pop(0)
        if next_move == "R":
            current_pos[1] += 1
        elif next_move == "L":
            current_pos[1] -= 1
        elif next_move == "U":
            current_pos[0] -= 1
        elif next_move == "D":
            current_pos[0] += 1

        # we now want to make sure that we add only valid entries to the path
        if current_pos[0] > 0:
            queue.append(path + "U")
        
            


our_queue = ""
our_maze = createSmallMaze()
print_maze(our_maze)
print(find_starting_pos(our_maze))
