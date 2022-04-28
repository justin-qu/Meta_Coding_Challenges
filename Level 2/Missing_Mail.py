## Problem: Missing Mail
## You are the manager of a mail room which is frequently subject to theft. A
## period of N days is about to occur, such that on the ith day, the following
## sequence of events will occur in order:

##  1. A package with a value of V{i} dollars will get delivered to the mail
##     room (unless V{i} = 0, in which case no package will get delivered).
##
##  2. You can choose to pay C dollars to enter the mail room and collect all of
##     the packages there (removing them from the room), and then leave the
##     room.
##
##  3. With probability S, all packages currently in the mail room will get
##     stolen (and therefore removed from the room).

## Note that you're aware of the delivery schedule V{1..N}, but can only observe
## the state of the mail room when you choose to enter it, meaning that you
## won't immediately be aware of whether or not packages were stolen at the end
## of any given day.

## Your profit after the Nth day will be equal to the total value of all
## packages which you collected up to that point, minus the total amount of
## money you spent on entering the mail room.

## Please determine the maximum expected profit you can achieve (in dollars).

## Note: Your return value must have an absolute or relative error of at most
## 10^(-6) to be considered correct.

## Constraints:
## 1 <= N <= 4000
## 0 <= V{i} <= 1000
## 1 <= C <= 1000
## 0.0 <= S <= 1.0

## Solution
## Time Complexity: O(N * N)
## Space Complexity: O(N * N)
## Explanation: Using dynamic programming, we can write a recursive function to
## solve this problem. On each day you have two choices, take or leave the
## packages. The maximum profit you could obtain on day i with packages starting
## from day j is:
##
##      today_profit = expected_mail_value(i, j) - C
##      max_profit(i, j) = max(max_profit(i + 1, i + 1) + today_profit,
##                             max_profit(i + 1, j))
##      max_profit(N, j) = 0
##      Original Problem: max_profit(0, 0)
##
## Rather than have expected_mail_value and max_profit be functions, we can
## precompute the values and save them in a matrix for lookup later.

from typing import List

def getMaxExpectedProfit(N: int, V: List[int], C: int, S: float) -> float:
    prob_packages_remain = 1 - S
    max_profit = [[0] * (N + 1) for _ in range(N + 1)]
    expected_mail_value = [[0] * (N + 1) for _ in range(N + 1)]

    ## Precompute the expected_mail_value lookup table.
    for j in range(N):
        expected_mail_value[j][j] = V[j]
        for i in range(j + 1, N):
            expected_mail_value[i][j] = V[i] + (expected_mail_value[i - 1][j] * prob_packages_remain)

    ## Compute the max_profit lookup table.
    for i in range(N - 1, -1 , -1):
        for j in range(i, -1, -1):
            max_profit[i][j] = max(max_profit[i+1][i+1] + expected_mail_value[i][j] - C,
                                   max_profit[i+1][j])

    ## Max profit on day zero
    return max_profit[0][0]

## Test Cases
if __name__ == "__main__":
    ## Test Case 1
    N = 5
    V = [10, 2, 8, 6, 4]
    C = 5
    S = 0.0

    print("Test Case 1")
    print("Expected Return Value = 25.0")
    print("Actual Return Value   = {}".format(getMaxExpectedProfit(N, V, C, S)))
    print("")

    ## Test Case 2
    N = 5
    V = [10, 2, 8, 6, 4]
    C = 5
    S = 1.0

    print("Test Case 2")
    print("Expected Return Value = 9.0")
    print("Actual Return Value   = {}".format(getMaxExpectedProfit(N, V, C, S)))
    print("")

    ## Test Case 3
    N = 5
    V = [10, 2, 8, 6, 4]
    C = 3
    S = 0.5

    print("Test Case 3")
    print("Expected Return Value = 17.0")
    print("Actual Return Value   = {}".format(getMaxExpectedProfit(N, V, C, S)))
    print("")
    
    ## Test Case 4
    N = 5
    V = [10, 2, 8, 6, 4]
    C = 3
    S = 0.15

    print("Test Case 4")
    print("Expected Return Value = 20.108250")
    print("Actual Return Value   = {}".format(getMaxExpectedProfit(N, V, C, S)))
    print("")
