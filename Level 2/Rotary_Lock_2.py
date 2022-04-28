## Problem: Rotary Lock 2
## You're trying to open a lock. The lock comes with two wheels, each of which
## has the integers from 1 to N arranged in a circle in order around it (with
## integers 1 and N adjacent to one another). Each wheel is initially pointing
## at 1.

## It takes 1 second to rotate the wheel by 1 unit to an adjacent integer in
## either direction, and it takes no time to select an integer once the wheel is
## pointing at it.

## The lock will open if you enter a certain code. The code consists of a
## sequence of M integers, the ith of which is C{i}. For each integer in the
## sequence, you may select it with either of the two wheels. Determine the
## minimum number of seconds required to select all M of the code's integers
## in order.

## Constraints:
## 3 <= N <= 1,000,000,000
## 1 <= M <= 3,000
## 1 <= C{i} <= N

## Solution
## Time Complexity: O(M * M)
## Space Complexity: O(M * M)
## Explanation: When entering the ith number in the code, there are i - 1
## possible states the lock could be in. One wheel must be set to C[i - 1] while
## the other wheel can be set to any of the previous numbers in the code or 1
## (the starting position). For each number in the code, we can compute the
## minimum amount of time it would take to complete the code from every i - 1
## possible states. The recursive form looks like:
##
##      ## The two wheels of the lock are set to C[i-1] and C[j]
##      ## For each state, we must to use one of the two wheels.
##      min_code_entry_time(i, j) = min(rotation_time(code[i - 1], code[i]) + min_code_entry_time[i + 1][j],
##                                      rotation_time(code[j], code[i]) + min_code_entry_time[i + 1][i - 1])

from typing import List

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    ## Compute the minimum time to rotate from c1 to c2
    def rotation_time(c1, c2):
        distance = abs(c1 - c2)
        return min(distance, N - distance)

    ## Inserting 1 at the beginning of the C simply makes the code cleaner
    ## Cost of O(M) time and space.
    code = [1] + C
    min_code_entry_time = [[0] * (M) for _ in range(M)]

    for i in range(M - 1, 0, -1):
        for j in range(i):
            ## This line looks slightly different to optimize memory usage
            min_code_entry_time[i - 1][j] = min(rotation_time(code[i], code[i + 1]) + min_code_entry_time[i][j],
                                                rotation_time(code[j], code[i + 1]) + min_code_entry_time[i][i])

    return rotation_time(1, C[0]) + min_code_entry_time[0][0]

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
    print("Expected Return Value = 6")
    print("Actual Return Value   = {}".format(getMinCodeEntryTime(N, M, C)))
    print("")
