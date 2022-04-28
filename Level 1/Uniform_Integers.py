## Problem: Uniform Integers
## A positive integer is considered uniform if all of its digits are equal. For
## example, 222 is uniform, while 223 is not.

## Given two positive integers A and B, determine the number of uniform integers
## between A and B, inclusive.

## Constraints:
## 1 <= A <= B <= 10^(12)

## Solution
## Time Complexity: O(log10(A * B)) == O(log10(A) + log10(B))
## Space Complexity: O(log10(A * B))
## Explanation: Given an uniform integer D, we can determine how many uniform
## integers are less than or equal to D in O(log10(D)) time. So to find the
## number of uniform integers between A and B, we just need to subtract the
## number of uniform integers less than B from the number of uniform integers
## less than A. To find the smallest uniform integer greater than A, we
## need to do is make a uniform integer by changing all of A's digits to A's
## first digit. For example, 2468753 becomes 2222222. If it is smaller than A
## then the next uniform integer will be greater than A. This takes O(log10(A))
## time for A and O(log10(B)) for B, resulting in O(log10(A) + log10(B)) time.

## Here's the pattern:
## 0 * 9 + 1 -> 1  |  1 * 9 + 1 -> 11  |  2 * 9 + 1 -> 111  |  3 * 9 + 1 -> 1111
## 0 * 9 + 2 -> 2  |  1 * 9 + 2 -> 22  |  2 * 9 + 2 -> 222  |  3 * 9 + 2 -> 2222
## 0 * 9 + 3 -> 3  |  1 * 9 + 3 -> 33  |  2 * 9 + 3 -> 333  |  3 * 9 + 3 -> 3333
## 0 * 9 + 4 -> 4  |  1 * 9 + 4 -> 44  |  2 * 9 + 4 -> 444  |  3 * 9 + 4 -> 4444
## 0 * 9 + 5 -> 5  |  1 * 9 + 5 -> 55  |  2 * 9 + 5 -> 555  |  3 * 9 + 5 -> 5555
## 0 * 9 + 6 -> 6  |  1 * 9 + 6 -> 66  |  2 * 9 + 6 -> 666  |  3 * 9 + 6 -> 6666
## 0 * 9 + 7 -> 7  |  1 * 9 + 7 -> 77  |  2 * 9 + 7 -> 777  |  3 * 9 + 7 -> 7777
## 0 * 9 + 8 -> 8  |  1 * 9 + 8 -> 88  |  2 * 9 + 8 -> 888  |  3 * 9 + 8 -> 8888
## 0 * 9 + 9 -> 9  |  1 * 9 + 9 -> 99  |  2 * 9 + 9 -> 999  |  3 * 9 + 9 -> 9999

def getUniformIntegerCountInInterval(A: int, B: int) -> int:
    first_uniform_int_id = 0
    last_uniform_int_id  = 0

    ## Convert integer to list of digits
    integer_digits = []
    while A > 0:
        integer_digits.append(A % 10)
        A = A // 10

    ## Loop through digits from left to right
    first_digit = integer_digits[-1]
    for i in range(len(integer_digits) - 2, -1, -1):
        ## The uniform integer is greater than A
        if integer_digits[i] < first_digit:
            break
        
        ## The uniform integer is less than A 
        if integer_digits[i] > first_digit:
            first_digit += 1
            break

    ## Map uniform integer to its counting ID
    first_uniform_int_id = (9 * (len(integer_digits) - 1)) + first_digit

    ## Convert integer to list of digits
    integer_digits = []
    while B > 0:
        integer_digits.append(B % 10)
        B = B // 10

    ## Loop through digits from left to right
    first_digit = integer_digits[-1]
    for i in range(len(integer_digits) - 2, -1, -1):
        ## The uniform integer is less than B 
        if integer_digits[i] > first_digit:
            break
        
        ## The uniform integer is greater than B
        if integer_digits[i] < first_digit:
            first_digit -= 1
            break

    ## Map uniform integer to its counting ID
    last_uniform_int_id = (9 * (len(integer_digits) - 1)) + first_digit

    return last_uniform_int_id - first_uniform_int_id + 1

## Test Cases
if __name__ == "__main__":
    ## Test Case 1
    A = 75
    B = 300

    print("Test Case 1")
    print("Expected Return Value = 5")
    print("Actual Return Value   = {}".format(getUniformIntegerCountInInterval(A, B)))
    print("")

    ## Test Case 2
    A = 1
    B = 9

    print("Test Case 2")
    print("Expected Return Value = 9")
    print("Actual Return Value   = {}".format(getUniformIntegerCountInInterval(A, B)))
    print("")

    ## Test Case 3
    A = 999999999999
    B = 999999999999


    print("Test Case 3")
    print("Expected Return Value = 1")
    print("Actual Return Value   = {}".format(getUniformIntegerCountInInterval(A, B)))
    print("")
