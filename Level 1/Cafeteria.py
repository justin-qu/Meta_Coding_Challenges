## Problem: Cafeteria
## A cafeteria table consists of a row of N seats, numbered from 1 to N from
## left to right. Social distancing guidelines require that every diner be
## seated such that K seats to their left and K seats to their right (or all the
## remaining seats to that side if there are fewer than K) remain empty.

## There are currently M diners seated at the table, the ith of whom is in seat
## S{i}. No two diners are sitting in the same seat, and the social distancing
## guidelines are satisfied.

## Determine the maximum number of additional diners who can potentially sit at
## the table without social distancing guidelines being violated for any new or
## existing diners, assuming that the existing diners cannot move and that the
## additional diners will cooperate to maximize how many of them can sit down.

## Constraints:
## 1 <= N <= 10^(15)
## 1 <= K <= N
## 1 <= M <= 500,000
## M <= N
## 1 <= S{i} <= N

## Solution
## Time Complexity: O(M * log(M))
## Space Complexity: O(M); O(1) if sorting is done in-place.
## Explanation: The number of additional diners between two seats can easily be
## calculated in O(1) time, but requires us to iterate through diners from left
## to right. So, sort the existing diners in O(M * log(M)) time and then sum up
## the number of additional diners that can be placed between each existing
## diner.

from typing import List

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    additional_diners = 0
    social_distance = K + 1

    current_diners = sorted(S)

    ## Calculate additional diners before the first diner.
    additional_diners += (current_diners[0] - 1) // social_distance

    ## Calculate additional diners after the last diner.
    additional_diners += (N - current_diners[-1]) // social_distance

    ## Calculate additional diners between each consecutive diner.
    for i in range(M - 1):
        diner1 = current_diners[i]
        diner2 = current_diners[i + 1]
        additional_diners += (diner2 - diner1 - social_distance) // social_distance

    return additional_diners

## Test Cases
if __name__ == "__main__":
    ## Test Case 1
    N = 10
    K = 1
    M = 2
    S = [2, 6]

    print("Test Case 1")
    print("Expected Return Value = 3")
    print("Actual Return Value   = {}".format(getMaxAdditionalDinersCount(N, K, M, S)))
    print("")

    ## Test Case 2
    N = 15
    K = 2
    M = 3
    S = [11, 6, 14]

    print("Test Case 2")
    print("Expected Return Value = 1")
    print("Actual Return Value   = {}".format(getMaxAdditionalDinersCount(N, K, M, S)))
    print("")
