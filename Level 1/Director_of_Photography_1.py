## Problem: Director of Photography 1
## A photography set consists of N cells in a row, numbered from 1 to N in
## order, and can be represented by a string C of length N. Each cell i is one
## of the following types (indicated by C{i}, the ith character of C):

##      If C{i} = 'P', it is allowed to contain a photographer
##      If C{i} = 'A', it is allowed to contain an actor
##      If C{i} = 'B', it is allowed to contain a backdrop
##      If C{i} = '.', it must be left empty

## A photograph consists of a photographer, an actor, and a backdrop, such that
## each of them is placed in a valid cell, and such that the actor is between
## the photographer and the backdrop. Such a photograph is considered artistic
## if the distance between the photographer and the actor is between X and Y
## cells (inclusive), and the distance between the actor and the backdrop is
## also between X and Y cells (inclusive). The distance between cells i and j
## is |i - j| (the absolute value of the difference between their indices).

## Determine the number of different artistic photographs which could
## potentially be taken at the set. Two photographs are considered different if
## they involve a different photographer cell, actor cell, and/or backdrop cell.

## Constraints:
## 1 <= N <= 200
## 1 <= X <= Y <= N

## Solution
## Time Complexity: O(N)
## Space Complexity: O(N)
## Explanation: See Director of Photography 2. The code is the exact same.

from typing import List

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    actors = []
    photos_before_pos = [0]
    bgs_before_pos = [0]
    photo_counter = 0
    bgs_counter = 0

    for i in range(N):
        if C[i] == 'A':
            actors.append(i)
        elif C[i] == 'P':
            photo_counter += 1
        elif C[i] == 'B':
            bgs_counter += 1

        ## thing_before_pos[i + 1] = thing_count 
        photos_before_pos.append(photo_counter)
        bgs_before_pos.append(bgs_counter)

    photograph_count = 0
    for actor_pos in actors:
        ## Left interval must be >= 0
        left_start = max(0, actor_pos - Y)
        left_end   = max(0, actor_pos - X + 1)

        ## Right interval must be <= N
        right_start = min(N, actor_pos + X)
        right_end   = min(N, actor_pos + Y + 1)

        ## Photographer - Actor - Background
        photograph_count += (photos_before_pos[left_end] - photos_before_pos[left_start]) \
                          * (bgs_before_pos[right_end] - bgs_before_pos[right_start])

        ## Background - Actor - Photographer
        photograph_count += (bgs_before_pos[left_end] - bgs_before_pos[left_start]) \
                          * (photos_before_pos[right_end] - photos_before_pos[right_start])

    return photograph_count

## Test Cases
if __name__ == "__main__":
    ## Test Case 1
    N = 5
    C = 'APABA'
    X = 1
    Y = 2

    print("Test Case 1")
    print("Expected Return Value = 1")
    print("Actual Return Value   = {}".format(getArtisticPhotographCount(N, C, X, Y)))
    print("")

    ## Test Case 2
    N = 5
    C = 'APABA'
    X = 2
    Y = 3

    print("Test Case 2")
    print("Expected Return Value = 0")
    print("Actual Return Value   = {}".format(getArtisticPhotographCount(N, C, X, Y)))
    print("")

    ## Test Case 3
    N = 8
    C = '.PBAAP.B'
    X = 1
    Y = 3

    print("Test Case 3")
    print("Expected Return Value = 3")
    print("Actual Return Value   = {}".format(getArtisticPhotographCount(N, C, X, Y)))
    print("")
