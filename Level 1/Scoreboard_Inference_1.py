## Problem: Scoreboard Inference 1
## You are spectating a programming contest with N competitors, each trying to
## independently solve the same set of programming problems. Each problem has a
## point value, which is either 1 or 2.

## On the scoreboard, you observe that the ith competitor has attained a score
## of S{i}, which is a positive integer equal to the sum of the point values of
## all the problems they have solved.

## The scoreboard does not display the number of problems in the contest, nor
## their point values. Using the information available, you would like to
## determine the minimum possible number of problems in the contest.

## Constraints:
## 1 <= N <= 500,000
## 1 <= S{i} <= 1,000,000,000

## Solution
## Time Complexity: O(N)
## Space Complexity: O(1)
## Explanation: If there is an odd score, there must be a 1-point problem. There
## is no point in having more than one 1-point problem, since two 1-point
## problems is equivalent to one 2-point problem. The minimum number of problems
## with a value of two is determined by the highest score since we will need
## exactly highest_score // 2 problems to achieve the highest score.

from typing import List

def getMinProblemCount(N: int, S: List[int]) -> int:
    contains_odd_score = 0
    highest_score = max(S)

    for score in S:
        if score % 2 == 1:
            contains_odd_score = 1
            break

    return highest_score // 2 + contains_odd_score

## Test Cases
if __name__ == "__main__":
    ## Test Case 1
    N = 6
    S = [1, 2, 3, 4, 5, 6]

    print("Test Case 1")
    print("Expected Return Value = 4")
    print("Actual Return Value   = {}".format(getMinProblemCount(N, S)))
    print("")

    ## Test Case 2
    N = 4
    S = [4, 3, 3, 4]

    print("Test Case 2")
    print("Expected Return Value = 3")
    print("Actual Return Value   = {}".format(getMinProblemCount(N, S)))
    print("")

    ## Test Case 3
    N = 4
    S = [2, 4, 6, 8]

    print("Test Case 3")
    print("Expected Return Value = 4")
    print("Actual Return Value   = {}".format(getMinProblemCount(N, S)))
    print("")
    
