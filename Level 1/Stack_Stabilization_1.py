## Problem: Stack Stabilization 1
## There's a stack of N inflatable discs, with the ith disc from the top having
## an initial radius of R{i} inches.

## The stack is considered unstable if it includes at least one disc whose
## radius is larger than or equal to that of the disc directly under it. In
## other words, for the stack to be stable, each disc must have a strictly
## smaller radius than that of the disc directly under it.

## As long as the stack is unstable, you can repeatedly choose any disc of your
## choice and deflate it down to have a radius of your choice which is strictly
## smaller than the disc’s prior radius. The new radius must be a positive
## integer number of inches.

## Determine the minimum number of discs which need to be deflated in order to
## make the stack stable, if this is possible at all. If it is impossible to
## stabilize the stack, return -1 instead.

## Constraints:
## 1 <= N <= 50
## 1 <= R{i} <= 1,000,000,000

## Solution
## Time Complexity: O(N)
## Space Complexity: O(1)
## Explanation: Since the dists must be positive integers, the ith disk must
## have a radius of at least i + 1 (R[0] >= 1). As long as this holds, iterate
## through R backwards and deflate disks to be 1 inch smaller than the disk
## below it if necessary.

from typing import List

def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
    deflate_count = 0
    prev_disk_size = R[-1]

    for i in range(N - 1, 0, -1):
        if R[i] <= i:
            return -1
        
        if R[i - 1] >= prev_disk_size:
            deflate_count += 1
            prev_disk_size = prev_disk_size - 1
        else:
            prev_disk_size = R[i - 1]

    return deflate_count

## Test Cases
if __name__ == "__main__":
    ## Test Case 1
    N = 5
    R = [2, 5, 3, 6, 5]

    print("Test Case 1")
    print("Expected Return Value = 3")
    print("Actual Return Value   = {}".format(getMinimumDeflatedDiscCount(N, R)))
    print("")

    ## Test Case 2
    N = 3
    R = [100, 100, 100]

    print("Test Case 2")
    print("Expected Return Value = 2")
    print("Actual Return Value   = {}".format(getMinimumDeflatedDiscCount(N, R)))
    print("")

    ## Test Case 3
    N = 4
    R = [6, 5, 4, 3]

    print("Test Case 3")
    print("Expected Return Value = -1")
    print("Actual Return Value   = {}".format(getMinimumDeflatedDiscCount(N, R)))
    print("")
