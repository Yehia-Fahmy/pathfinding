# pathfinding
An algorithm to find the shortest path to a given maze
By: Yehia Fahmy

pathfind.py will take a 2-D array defined in createMaze()
- start point definded by "O"
- end point defined by "X"
- obsticals defined by "#"

The algorithm works as follows:
1. Create a queue to hold all the paths to be taken from the starting path

2. Take a path from the front of the queue and check to see if it has found the end point

3. If it hasnt found the endpoint it will add an extra move to that path and place it at the end of the queue

4. After adding to the queue the algorithm will then repeat with a path that is at the front of the queue