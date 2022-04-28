## Problem: Scoreboard Inference 2
## You are spectating a programming contest with N competitors, each trying to
## independently solve the same set of programming problems. Each problem has a
## point value, which is either 1, 2 or 3.

## On the scoreboard, you observe that the iith competitor has attained a score
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
## Explanation: This problem is mostly the same as the level 1 version. The
## minimum number of problems needed is primarily limited by the highest score.
## However depending on what scores are in S (and what scores are not), we may
## be able to optimize point values and reduce the number of problems needed by
## 1. We iterate through S once and maintain the top two scores in O(N).
## Remaining computations are O(1).

from typing import List

def getMinProblemCount(N: int, S: List[int]) -> int:
    has_score_of_one = False
    contains_one_point_problem = 0
    contains_two_point_problem = 0

    largest_score = 0
    second_largest_score = 0

    ## Scan S and set flags if certain scores are seen.
    for score in S:
        if score % 3 == 1:
            contains_one_point_problem = 1
            if score == 1:
                has_score_of_one = True
        elif score % 3 == 2:
            contains_two_point_problem = 1

        if score > second_largest_score:
            if score > largest_score:
                largest_score, second_largest_score = score, largest_score
            elif score < largest_score:
                second_largest_score = score

    ## This is our upper-bound
    problem_count = (largest_score // 3) + contains_one_point_problem + contains_two_point_problem

    ## Remove an extraneous 3-point problem
    if largest_score % 3 == 0 and contains_one_point_problem and contains_two_point_problem:
        problem_count -= 1
    ## Replace the 1-point problem with a 2-point problem and remove an extraneous 3-point problem.
    elif not has_score_of_one and contains_one_point_problem:
        if largest_score % 3 == 1 and second_largest_score != largest_score - 1:
            problem_count -= 1

    return problem_count

## Test Cases
if __name__ == "__main__":
    ## Test Case 1
    N = 5
    S = [1, 2, 3, 4, 5]

    print("Test Case 1")
    print("Expected Return Value = 3")
    print("Actual Return Value   = {}".format(getMinProblemCount(N, S)))
    print("")

    ## Test Case 2
    N = 4
    S = [4, 3, 3, 4]

    print("Test Case 2")
    print("Expected Return Value = 2")
    print("Actual Return Value   = {}".format(getMinProblemCount(N, S)))
    print("")

    ## Test Case 3
    N = 4
    S = [2, 4, 6, 8]

    print("Test Case 3")
    print("Expected Return Value = 4")
    print("Actual Return Value   = {}".format(getMinProblemCount(N, S)))
    print("")
    
    ## Test Case 4
    N = 1
    S = [8]

    print("Test Case 4")
    print("Expected Return Value = 3")
    print("Actual Return Value   = {}".format(getMinProblemCount(N, S)))
    print("")
