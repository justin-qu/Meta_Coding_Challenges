## Problem: Kaitenzushi
## There are N dishes in a row on a kaiten belt, with the ith dish being of type
## D{i}. Some dishes may be of the same type as one another.

## Kaiten Belt: {https://en.wikipedia.org/wiki/Conveyor_belt_sushi}

## You're very hungry, but you'd also like to keep things interesting. The N
## dishes will arrive in front of you, one after another in order, and for each
## one you'll eat it as long as it isn't the same type as any of the previous K
## dishes you've eaten. You eat very fast, so you can consume a dish before the
## next one gets to you. Any dishes you choose not to eat as they pass will be
## eaten by others.

## Determine how many dishes you'll end up eating.

## Constraints:
## 1 <= N <= 500,000
## 1 <= K <= N
## 1 <= D{i} <= 1,000,000

## Solution
## Time Complexity: O(N * K); O(N) on average
## Space Complexity: O(K)
## Explanation: By using a circular list, we can keep track of the last K dishes
## we eat and add new dishes in O(1) time. Checking is a new dish is in this
## takes O(K) time, so we use a set to do lookups in O(1) time on average. At
## the cost of O(D) space, we could use a list of booleans to guarantee O(N)
## lookup times.

from typing import List

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
    dishes_to_skip = set()
    dish_history = [None] * K
    index = 0
    dish_count = 0

    for dish in D:
        if dish not in dishes_to_skip:
            dish_count += 1
            dishes_to_skip.add(dish)
            dishes_to_skip.discard(dish_history[index])
            dish_history[index] = dish
            index = (index + 1) % K

    return dish_count

## Test Cases
if __name__ == "__main__":
    ## Test Case 1
    N = 6
    D = [1, 2, 3, 3, 2, 1]
    K = 1

    print("Test Case 1")
    print("Expected Return Value = 5")
    print("Actual Return Value   = {}".format(getMaximumEatenDishCount(N, D, K)))
    print("")

    ## Test Case 2
    N = 6
    D = [1, 2, 3, 3, 2, 1]
    K = 2

    print("Test Case 2")
    print("Expected Return Value = 4")
    print("Actual Return Value   = {}".format(getMaximumEatenDishCount(N, D, K)))
    print("")

    ## Test Case 3
    N = 7
    D = [1, 2, 1, 2, 1, 2, 1]
    K = 2

    print("Test Case 3")
    print("Expected Return Value = 2")
    print("Actual Return Value   = {}".format(getMaximumEatenDishCount(N, D, K)))
    print("")
