## Problem: Stack Stabilization 2
## There's a stack of N inflatable discs, with the ith disc from the top having 
## an initial radius of R{i} inches.

## The stack is considered unstable if it includes at least one disc whose radius 
## is larger than or equal to that of the disc directly under it. In other words, 
## for the stack to be stable, each disc must have a strictly smaller radius than 
## that of the disc directly under it.

## As long as the stack is unstable, you can repeatedly choose a disc and perform 
## one of the following operations:

## - Inflate the disc, increasing its radius by 1 inch. This operation takes A 
##   seconds and may be performed on discs of any radius (even those that exceed 
##   10^9 inches).

## - Deflate the disc, decreasing its radius by 1 inch. This operation takes B 
##   seconds and may only be performed if the resulting radius is a positive 
##   integer number of inches (that is, if the disc has a radius of at least 2 before 
##   being deflated).

## Determine the minimum number of seconds needed in order to make the stack stable.

## Constraints:
## 1 <= N <= 50
## 1 <= R{i} <= 1,000,000,000
## 1 <= A, B <= 100

## Solution
## Time Complexity: O(N * N)
## Space Complexity: O(N)
## Explanation: First, we can redefine the problem. Instead of finding a stack where
## each ring must be greater than the ring before it, we solve for a stack J{i} where 
## J{i} = R{i} - i and each ring must be greater than OR EQUAL to the ring before.

## Another key to this algorithm is realizing that we only need to compute the times 
## to stabilize the stack to the values in the stack. Below is a diagram showing the
## cost to set all rings to the same radius. The example is just to illustrate 
## linearity, it is not correct since it needlessly raises every ring to some radius 
## R even if the stack is already stable and less than R.

##                                            Cost of Stack    Cost of J{i}
##           |                                                                Y = -2A(X - J{0})                + 3A  for         X <= J{0}
##    J{0} * |                                0                3A             Y =  -A(X - J{1}) +  B(X - J{0}) + 0   for J{0} <= X <= J{1}
##           |                                B                2A             Y =                 2B(X - J{1}) + 3B  for J{1} <= X
##           |                                2B               A
##    -------| J{1} *                         3B               0

##                                            Cost of Stack    Cost of J{i}
##                   |                                                        Y = -3A(X - J{0})                + 5A  for         X <= J{0}
##    J{0} *         |                        3A               2A             Y = -2A(X - J{2}) +  B(X - J{0}) +  A  for J{0} <= X <= J{2}
##                   |                        2A + B           A              Y =  -A(X - J{1}) + 2B(X - J{2}) + 2B  for J{2} <= X <= J{1}
##    ---------------| J{2} *                 A + 2B           0              Y =                 3B(X - J{1}) + 4B  for J{1} <= X
##            J{1} * |                        3B               B

##                                            Cost of Stack    Cost of J{i}
##                           |                                                Y = -4A(X - J{0})                + 6A      for         X <= J{0}
##    J{0} *                 |                5A               A              Y = -3A(X - J{3}) +  B(X - J{0}) + 3A      for J{0} <= X <= J{3}
##    -----------------------| J{3} *         3A + B           0              Y = -2A(X - J{2}) + 2B(X - J{3}) +  A +  B for J{3} <= X <= J{2}
##                    J{2} * |                A + 2B           B              Y =  -A(X - J{1}) + 3B(X - J{2}) + 3B      for J{2} <= X <= J{1}
##            J{1} *         |                4B               2B             Y =                 4B(X - J{1}) + 6B      for J{1} <= X 

## From the example illustrated, we can see that for each ring, we are repeatedly adding 
## the piecewise function:
## {
##     Y = -a(X - J{i}) for X <= R{i}
##     Y =  b(X - J{i}) for X >= R{i}
## }
##
## Given two linear functions F(X) and G(X), H(X) = F(X) + G(X) is also linear. Since the 
## cost function is always linear between two adjacent radii, the minimum cost must be at 
## one of radii in R.  Now, we can iteratively find the minimum time needed to stabilize 
## the stack up the ith. Since we don't know what radius is optimal, we compute the 
## minimum cost to create a stable stack for every radius K, where K is the sorted list of
## all J{i} > 0.
##
##      ## The minimum time to stabilize the stack up to the ith ring with a maximum radius
##      ## less than or equal to K{j} is equal to the minimum of the cost to stabilize 
##      ## the stack up to the ith ring for any radius K{i} <= K{j} and the cost to stabilize
##      ## the stack up to the (i-1)th ring with maximum radius K{j} and the cost to
##      ## inflate/deflate J{i} to K{j}. If K is sorted in ascending order, this can be
##      ## simplified to the following.
##      min_stable_time(i, j) = min(min_stable_time(i-1, j) + cost_to_flate(J{i}, K{j}), min_stable_time(i, j-1))

from typing import List
# Write any import statements here

def getMinimumSecondsRequired(N: int, R: List[int], A: int, B: int) -> int:
    ## Redefine Problem
    R = [r - i for i, r in enumerate(R)]

    ## Get Key Radii
    key_radii = {max(1, r) for r in R}
    key_radii = list(key_radii)
    key_radii.sort()
  
    cost_for_radius = [0] * len(key_radii)
    for r in R:
        for i, key_radius in enumerate(key_radii):
            delta = key_radius - r
            cost = 0
            
            if delta > 0:
                cost = delta * A
            else:
                cost = -delta * B
            
            if i == 0:
                cost_for_radius[0] += cost
            else:
                cost_for_radius[i] = min(cost_for_radius[i-1], cost_for_radius[i] + cost)
        
    return cost_for_radius[-1]

## Test Cases
if __name__ == "__main__":
    ## Test Case 1
    N = 5
    R = [2, 5, 3, 6, 5]
    A = 1
    B = 1

    print("Test Case 1")
    print("Expected Return Value = 5")
    print("Actual Return Value   = {}".format(getMinimumSecondsRequired(N, R, A, B)))
    print("")

    ## Test Case 2
    N = 3
    R = [100, 100, 100]
    A = 2
    B = 3
    print("Test Case 2")
    print("Expected Return Value = 5")
    print("Actual Return Value   = {}".format(getMinimumSecondsRequired(N, R, A, B)))
    print("")

    ## Test Case 3
    N = 3
    R = [100, 100, 100]
    A = 7
    B = 3
    print("Test Case 3")
    print("Expected Return Value = 9")
    print("Actual Return Value   = {}".format(getMinimumSecondsRequired(N, R, A, B)))
    print("")

    ## Test Case 4
    N = 4
    R = [6, 5, 4, 3]
    A = 10
    B = 1
    print("Test Case 4")
    print("Expected Return Value = 19")
    print("Actual Return Value   = {}".format(getMinimumSecondsRequired(N, R, A, B)))
    print("")

    ## Test Case 5
    N = 4
    R = [100, 100, 1, 1]
    A = 2
    B = 1
    print("Test Case 5")
    print("Expected Return Value = 207")
    print("Actual Return Value   = {}".format(getMinimumSecondsRequired(N, R, A, B)))
    print("")

    ## Test Case 6
    N = 6
    R = [6, 5, 2, 4, 4, 7]
    A = 1
    B = 1
    print("Test Case 6")
    print("Expected Return Value = 10")
    print("Actual Return Value   = {}".format(getMinimumSecondsRequired(N, R, A, B)))
    print("")
