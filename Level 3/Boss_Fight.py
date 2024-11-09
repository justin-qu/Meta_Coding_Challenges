## Problem: Boss Fight
## There are N warriors, the ith of which has a health of H{i} units and can 
## deal D{i} units of damage per second. The are confronting a boss who has
## unlimited health and can deal B units of damage per second. Both the 
## warriors and the boss deal damage continuously - for example, in half a
## second, the bossdeals B/2 units of damage.

## The warriors feel it would be unfair for many of them to fight the boss at 
## once, so they'll select just two representatives to go into battle. One 
## warrior {i} will be the front line and a different warrior {j} will back
## them up. During the battle, the boss will attack warrior {i} until that
## warrior is defeated (that is until the boss has dealt H{i} units of damage to
## them), and will then attack warrior {j} until that warrior is also defeated,
## at which point the battle will end. Along the way, each of the two warriors
## will do damage to the boss as long as they are undefeated.

## Of course, the warriors will never prevail, but they'd like to determine the 
## maximum amount of damage they could deal to the boss for any choice of warriors
## {i} and {j} before the battle ends.

## Constraints:
## 2 <= N <= 500,000
## 1 <= H{i} <= 1,000,000,000
## 1 <= D{i} <= 1,000,000,000
## 1 <= B <= 1,000,000,000

## Solution
## Time Complexity: O(N*N)
## Space Complexity: O(1)
## Explanation: Despite the worst-case time complexity of O(N^2), this algorithm
## usually finds the correct solution in O(N). We can make really good guesses
## about the best warriors simply by picking a random warrior {A}, and finding
## the best warrior {B} to partner warrior {A}. Repeat this process with warrior
## {B} to find warrior {C} and so on until the maximum damage stops increasing.

from typing import List

def getMaxDamageDealt(N: int, H: List[int], D: List[int], B: int) -> float:
    ## Precompute H{i}*D{i} for each warrior {i}
    C = [h * d for h, d in zip(H, D)]
  
    max_damage = 0
    best_warrior = 0
  
    run = True
    while run:
        run = False
        next_best_warrior = 0
    
        for i in range(N):
            if i == best_warrior:
                continue
        
            damage = C[best_warrior] + C[i] + max(H[best_warrior] * D[i], H[i] * D[best_warrior])
            if damage > max_damage:
                run = True
                max_damage = damage
                next_best_warrior = i
    
        best_warrior = next_best_warrior
    
    return max_damage / B

## Test Cases
if __name__ == "__main__":
    ## Test Case 1
    N = 3
    H = [2, 1, 4]
    D = [3, 1, 2]
    B = 4

    print("Test Case 1")
    print("Expected Return Value = 6.5")
    print("Actual Return Value   = {}".format(getMaxDamageDealt(N, H, D, B)))
    print("")

    ## Test Case 2
    N = 4
    H = [1, 1, 2, 100]
    D = [1, 2, 1, 3]
    B = 8
    
    print("Test Case 2")
    print("Expected Return Value = 62.75")
    print("Actual Return Value   = {}".format(getMaxDamageDealt(N, H, D, B)))
    print("")

    ## Test Case 3
    N = 4
    H = [1, 1, 2, 3]
    D = [1, 2, 1, 100]
    B = 8
    
    print("Test Case 3")
    print("Expected Return Value = 62.75")
    print("Actual Return Value   = {}".format(getMaxDamageDealt(N, H, D, B)))
    print("")
