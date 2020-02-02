import queue


def createMaze():
    maze = []
    maze.append(["#", "#", "#", "#", "#", "O", "#", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", "#", " ", "#", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", "X", "#", "#", "#", "#", "#", "#", "#"])

    return maze


def createMaze2():
    maze = []
    maze.append(["#", "#", "#", "#", "#", "#", "#", "O", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", "#", " ", "#", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", " ", " ", "#", " ", " ", " ", "#"])
    maze.append(["#", "X", "#", "#", "#", "#", "#", "#", "#"])

    return maze


def print_maze(maze):  # function to print the maze as it is
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            print(maze[i][j], end="")
            print(" ", end="")
        print()


def valid(maze, moves):  # function to check if a given path is valid on a given maze
    start_point = (0, 0)
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "O":
                start_point = [
                    i,
                    j,
                ]  # finds the starting point of the maze and stores it as (col, row)
            else:
                pass
    # now we want to find the current pos after following the path proposed
    current_point = start_point
    for move in moves:
        if move == "L":
            current_point[1] -= 1
        elif move == "R":
            current_point[1] += 1
        elif move == "U":
            current_point[0] -= 1
        elif move == "D":
            current_point[0] += 1

    if not (
        0 <= current_point[0] <= len(maze) - 1
        and 0 <= current_point[1] <= len(maze[0]) - 1
    ):  # checks to see if the current point is in the maze
        return False
    elif (
        maze[current_point[0]][current_point[1]] == "#"
    ):  # checks to see if the current point is blocked by an obstical
        return False

    return True  # returning true means the path is valid


def findEnd(maze, moves):
    start_point = (0, 0)
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "O":
                start_point = [
                    i,
                    j,
                ]  # finds the starting point of the maze and stores it as (col, row)
            else:
                pass

    current_point = (
        start_point
    )  # now we have our current point we have to use similar logic as before to determine our current point
    for move in moves:
        if move == "L":
            current_point[1] -= 1
        elif move == "R":
            current_point[1] += 1
        elif move == "U":
            current_point[0] -= 1
        elif move == "D":
            current_point[0] += 1
    # our current point is now determined we can check and see if we have found the target
    if maze[current_point[0]][current_point[1]] == "X":
        print("The path is: ", moves)  # if we have found a path we display it
        return True

    return False  # if no path has been found then we return false


"""
Functions we need:
- createMaze
- findEnd
- valid
- printMaze
"""

nums = queue.Queue()
nums.put("")
add = ""
maze = createMaze()
print("The maze looks like:")
print_maze(maze)

while not findEnd(maze, add):
    add = nums.get()
    # print(add)
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if valid(maze, put):
            nums.put(put)

