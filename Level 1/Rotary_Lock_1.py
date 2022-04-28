## Problem: Rotary Lock 1
## You're trying to open a lock. The lock comes with a wheel which has the
## integers from 1 to N arranged in a circle in order around it (with integers
## 1 and N adjacent to one another). The wheel is initially pointing at 1.

## It takes 1 second to rotate the wheel by 1 unit to an adjacent integer in
## either direction, and it takes no time to select an integer once the wheel
## is pointing at it.

## The lock will open if you enter a certain code. The code consists of a
## sequence of M integers, the ith of which is C{i}. Determine the minimum
## number of seconds required to select all M of the code's integers in order.

## Constraints:
## 3 <= N <= 50,000,000
## 1 <= M <= 1,000
## 1 <= C{i} <= N

## Solution
## Time Complexity: O(M)
## Space Complexity: O(1)
## Explanation: It takes O(1) time to calculate the number seconds it takes to
## rotate from A -> B. We compute this once for each integer in the code and
## there are M integers in the code.

from typing import List

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    ## Return the minimum time to rotate from c1 to c2
    def rotation_time(c1, c2):
        distance = abs(c1 - c2)
        return min(distance, N - distance)
    
    code_entry_time = rotation_time(1, C[0])

    for i in range(len(C) - 1):
        code_entry_time += rotation_time(C[i], C[i + 1])

    return code_entry_time

## Test Cases
if __name__ == "__main__":
    ## Test Case 1
    N = 3
    M = 3
    C = [1, 2, 3]

    print("Test Case 1")
    print("Expected Return Value = 2")
    print("Actual Return Value   = {}".format(getMinCodeEntryTime(N, M, C)))
    print("")

    ## Test Case 2
    N = 10
    M = 4
    C = [9, 4, 4, 8]

    print("Test Case 2")
    print("Expected Return Value = 11")
    print("Actual Return Value   = {}".format(getMinCodeEntryTime(N, M, C)))
    print("")
