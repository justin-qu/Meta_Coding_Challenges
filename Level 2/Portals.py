## Problem: Portals
## You've found yourself in a grid of cells with R rows and C columns. The cell
## in the ith row from the top and jth column from the left contains one of the
## following (indicated by the character G{i,j}:

##  -   If G{i,j} = '.', the cell is empty.
##  -   If G{i,j} = 'S', the cell contains your starting position. There is
#       exactly one such cell.
##  -   If G{i,j} = 'E', the cell contains an exit. There is at least one such
##      cell.
##  -   If G{i,j} = '#', the cell contains a wall.
##  -   Otherwise, if G{i,j} is a lowercase letter (between "a" and "z",
##      inclusive), the cell contains a portal marked with that letter.

## Your objective is to reach any exit from your starting position as quickly as
## possible. Each second, you may take either of the following actions:

##  -   Walk to a cell adjacent to your current one (directly above, below, to
##      the left, or to the right), as long as you remain within the grid and
##      that cell does not contain a wall.
##  -   If your current cell contains a portal, teleport to any other cell in
##      the grid containing a portal marked with the same letter as your current
##      cell's portal.

## Determine the minimum number of seconds required to reach any exit, if it's
## possible to do so at all. If it's not possible, return -1 instead.

## Constraints:
## 1 <= R, C <= 50
## G{i,j} ∈ {'.', 'S', 'E', '#', 'a' ... 'z'}

## Solution
## Time Complexity: O(R * C)
## Space Complexity: O(R * C)
## Explanation: This is a simple breadth-first search problem. The only
## difference between this an a basic grid search is that we need to consider
## portals as adjacent cells when standing on a portal.

from typing import List

def getSecondsRequired(R: int, C: int, G: List[List[str]]) -> int:
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"

    
    queue = []
    portals = dict()
    time_to_tile = [[0] * C for _ in range(R)]
    index = 0
    
    for letter in ALPHABET:
        portals[letter] = []

    ## Preprocessing
    for i in range(R):
        for j in range(C):
            tile = G[i][j]
            if tile == 'S':
                ## Put start as first element in queue
                queue.append((i, j))
            elif tile == 'E':
                pass
            elif tile == '.':
                pass
            elif tile == '#':
                ## Set to -1 so that we don't visit them. 0 is unvisited.
                time_to_tile[i][j] = -1
            else:
                ## Compile list of cells corresponding to each portal letter
                portals[tile].append((i, j))

    ## Rather than pop items off the beginnning of the queue, which is O(len(queue))
    ## simply increment index, which is a variable that points to the "first" item
    ## in the queue
    while index < len(queue):
        i, j = queue[index]
        current_tile = G[i][j]
        current_time = time_to_tile[i][j]
        index += 1

        if current_tile == 'E':
            return current_time

        ## Check cell below
        if i < R - 1:
            if time_to_tile[i + 1][j] == 0:
                queue.append((i + 1, j))
                time_to_tile[i + 1][j] = current_time + 1

        ## Check cell above
        if i > 0:
            if time_to_tile[i - 1][j] == 0:
                queue.append((i - 1, j))
                time_to_tile[i - 1][j] = current_time + 1

        ## Check cell to the right
        if j < C - 1:
            if time_to_tile[i][j + 1] == 0:
                queue.append((i, j + 1))
                time_to_tile[i][j + 1] = current_time + 1

        ## Check cell to the left
        if j > 0:
            if time_to_tile[i][j - 1] == 0:
                queue.append((i, j - 1))
                time_to_tile[i][j - 1] = current_time + 1

        ## Check connecting portals if standing on a portal
        if current_tile in portals and len(portals[current_tile]) > 0:
            for x, y in portals[current_tile]:
                if time_to_tile[x][y] == 0:
                    queue.append((x, y))
                    time_to_tile[x][y] = current_time + 1

            ## We don't need to check any of the portals again
            portals[current_tile] = []
                    
    return -1

## Test Cases
if __name__ == "__main__":
    ## Test Case 1
    R = 3
    C = 3
    G = [['.', 'E', '.'],
         ['.', '#', 'E'],
         ['.', 'S', '#']]

    print("Test Case 1")
    print("Expected Return Value = 4")
    print("Actual Return Value   = {}".format(getSecondsRequired(R, C, G)))
    print("")

    ## Test Case 2
    R = 3
    C = 4
    G = [['a', '.', 'S', 'a'],
         ['#', '#', '#', '#'],
         ['E', 'b', '.', 'b']]

    print("Test Case 2")
    print("Expected Return Value = -1")
    print("Actual Return Value   = {}".format(getSecondsRequired(R, C, G)))
    print("")

    ## Test Case 3
    R = 3
    C = 4
    G = [['a', 'S', '.', 'b'],
         ['#', '#', '#', '#'],
         ['E', 'b', '.', 'a']]

    print("Test Case 3")
    print("Expected Return Value = 4")
    print("Actual Return Value   = {}".format(getSecondsRequired(R, C, G)))
    print("")
    
    ## Test Case 4
    R = 1
    C = 9
    G = [['x', 'S', '.', '.', 'x', '.', '.', 'E', 'x']]

    print("Test Case 4")
    print("Expected Return Value = 3")
    print("Actual Return Value   = {}".format(getSecondsRequired(R, C, G)))
    print("")
