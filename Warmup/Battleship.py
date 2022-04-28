## Problem: Battleship
## You're playing Battleship on a grid of cells with R rows and C columns. There
## are 0 or more battleships on the grid, each occupying a single distinct cell.
## The cell in the ith row from the top and jth column from the left either
## contains a battleship (G{i,j} = 1) or doesn't (G{i,j} = 0).

## You're going to fire a single shot at a random cell in the grid. You'll
## choose this cell uniformly at random from the R * C possible cells. You're
## interested in the probability that the cell hit by your shot contains a
## battleship.

## Your task is to implement the function getHitProbability(R, C, G) which
## returns this probability.

## Note: Your return value must have an absolute or relative error of at most
## 10^(-6) to be considered correct.

## Constraints:
## 1 <= R, C <= 100
## G{i,j} ∈ {0, 1}

## Solution
## Time Complexity: O(R * C)
## Space Complexity: O(1)
## Explanation: Count the number of ships and divide by the total number of
## cells. Because the cells are either 0 or 1, the number of ships is the same
## as the sum of all the cells.

from typing import List

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
    num_ships = 0
  
    for row in G:
        num_ships += sum(row)
  
    return num_ships / (R * C)

## Test Cases
if __name__ == "__main__":
    ## Test Case 1
    R = 2
    C = 3
    G = [[0, 0, 1],
         [1, 0, 1]]

    print("Test Case 1")
    print("Expected Return Value = 0.5")
    print("Actual Return Value   = {}".format(getHitProbability(R, C, G)))
    print("")

    ## Test Case 2
    R = 2
    C = 2
    G = [[1, 1],
         [1, 1]]

    print("Test Case 2")
    print("Expected Return Value = 1.0")
    print("Actual Return Value   = {}".format(getHitProbability(R, C, G)))
    print("")
