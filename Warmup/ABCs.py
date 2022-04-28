## Problem: ABCs
## Given three integers A, B, and C, determine their sum.

## Your task is to implement the function getSum(A, B, C) which returns the sum
## A + B + C.

## Constraints:
## 1 <= A, B, C <= 100

## Solution
## Time Complexity: O(1)
## Space Complexity: O(1)
## Explanation: None

def getSum(A: int, B: int, C: int) -> int:
    return A + B + C

## Test Cases
if __name__ == "__main__":
    ## Test Case 1
    A = 1
    B = 2
    C = 3

    print("Test Case 1")
    print("Expected Return Value = 6")
    print("Actual Return Value   = {}".format(getSum(A, B, C)))
    print("")

    ## Test Case 2
    A = 100
    B = 100
    C = 100

    print("Test Case 2")
    print("Expected Return Value = 300")
    print("Actual Return Value   = {}".format(getSum(A, B, C)))
    print("")

    ## Test Case 3
    A = 85
    B = 16
    C = 93

    print("Test Case 3")
    print("Expected Return Value = 194")
    print("Actual Return Value   = {}".format(getSum(A, B, C)))
    print("")
