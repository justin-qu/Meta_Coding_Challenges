## Problem: Hops
## A family of frogs in a pond are traveling towards dry land to hibernate. They
## hope to do so by hopping across a trail of N lily pads, numbered from 1 to N
## in order.

## There are F frogs, numbered from 1 to F. Frog i is currently perched atop
## lily pad P{i}. No two frogs are currently on the same lily pad. Lily pad N is
## right next to the shore, and none of the frogs are initially on lily pad N.

## Each second, one frog may hop along the trail towards lily pad N. When a frog
## hops, it moves to the nearest lily pad after its current lily pad which is
## not currently occupied by another frog (hopping over any other frogs on
## intermediate lily pads along the way). If this causes it to reach lily pad N,
## it will immediately exit onto the shore. Multiple frogs may not
## simultaneously hop during the same second.

## Assuming the frogs work together optimally when deciding which frog should
## hop during each second, determine the minimum number of seconds required for
## all F of them to reach the shore.

## Constraints:
## 2 <= N <= 10^(12)
## 1 <= F <= 500,000
## 1 <= P{i} <= N - 1

## Solution
## Time Complexity: O(F)
## Space Complexity: O(1)
## Explanation: If we always have the frog farthest from the shore jump, the
## distance of the frog farthest from from shore always decreases by one every
## second. It is also impossible for the distance of the farthest frog to
## decrease by more than one every second. In the end, when all frogs are on
## shore, the distance of the farthest frog is zero. So the minimum amount of
## time it takes to get all frogs to shore is the same as the starting distance
## of the farthest frog.

from typing import List

def getSecondsRequired(N: int, F: int, P: List[int]) -> int:
    return N - min(P)

## Test Cases
if __name__ == "__main__":
    ## Test Case 1
    N = 3
    F = 1
    P = [1]

    print("Test Case 1")
    print("Expected Return Value = 2")
    print("Actual Return Value   = {}".format(getSecondsRequired(N, F, P)))
    print("")

    ## Test Case 2
    N = 6
    F = 3
    P = [5, 2, 4]

    print("Test Case 2")
    print("Expected Return Value = 4")
    print("Actual Return Value   = {}".format(getSecondsRequired(N, F, P)))
    print("")
