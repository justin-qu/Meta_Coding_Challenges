## Problem: Slippery Trip
## There's a grid of cells with R rows (numbered from 1 to R from top to bottom)
## and C columns (numbered from 1 to C from left to right). The grid wraps
## around horizontally, meaning that column 1 is just to the right of column C
## (and column C is just to the left of column 1).

## The cell in row i and column j initially contains one of the following
## (indicated by the character G{i,j}):

##      If G{i,j} = '.', the cell is empty.
##      If G{i,j} = '*', the cell contains a coin.
##      If G{i,j} = '>', the cell contains an arrow pointing right.
##      If G{i,j} = 'v', the cell contains an arrow pointing down.

## You may cyclically shift each row to the right as many times as you'd like
## (including not at all). Each such shift causes each of the row's cells to
## move 1 column to the right, with its rightmost cell (in column C) wrapping
## around and moving to column 1.

## After you've finished rotating the rows to your liking, you'll take a trip
## through the grid, starting by entering the cell at the top-left corner (in
## row 11 and column 11) downward from above the grid. Upon entering a cell, if
## it contains a coin that you haven't yet collected, you'll collect it. If it
## contains an arrow, your direction of travel will change to that of the arrow
## (either right or down). Either way, you'll then proceed to the next adjacent
## cell in your direction of travel. If you move rightward from column C, you'll
## wrap around to column 1 in the same row, and if you move downward from row R,
## you'll end your trip. Note that you may only collect each cell's coin at most
## once, that your trip might last forever, and that once you begin your trip
## you cannot shift the grid's rows further.

## Determine the maximum number of coins you can collect on your trip.

## Constraints:
## 2 <= R, C <= 400,000
## R * C <= 800,000
## G{i, j} ∈ {'.', '*', '>', 'v'}

## Solution
## Time Complexity: O(R * C)
## Space Complexity: O(R * C)
## Explanation: In O(C) time, we can iterate through a row and determine the
## maximum number of coins obtainable from the row, whether or not it contains a
## down arrow, and whether or not it only contains right arrows. Using this
## information from each row, we can compute the maximum amount of coins we can
## obtain over all rows. If the row contains a down arrow, then we can simply
## the maximum number of coins obtainable from the row. If it does not, then we
## should decide whether to pass the row by moving down through tile that is
## not a right arrow (but preferably a coin) or taking all the coins in the row
## and ending our run. 

from typing import List

def getMaxCollectableCoins(R: int, C: int, G: List[List[str]]) -> int:
    def process_row(row):
        max_coins_obtainable = 0
        is_terminal = False
        is_end = False
        
        coins_before_index = [0]
        coin_counter = 0
        
        contains_right_arrow = False
        right_arrow_index = -1
        first_down_index = -1

        for i in range(C):
            if row[i] == '*':
                coin_counter += 1
            elif row[i] == '>':
                contains_right_arrow = True
                if right_arrow_index == -1:
                    right_arrow_index = i
            elif row[i] == 'v':
                if first_down_index == -1:
                    first_down_index = i
                if right_arrow_index != -1:
                    ## If we have encountered a right arrow before this down
                    ## arrow, compute the number of coins between them and set
                    ## the max accordingly.
                    max_coins_obtainable = max(max_coins_obtainable,
                                               coins_before_index[i] - coins_before_index[right_arrow_index])
                    right_arrow_index = -1

            coins_before_index.append(coin_counter)
        
        if contains_right_arrow == True:
            if first_down_index == -1:
                ## Row contains a right arrow but no down arrow. This means that
                ## if we take the right arrow, we will loop in this row 
                ## indefinitely, obtaining all the coins and ending the run.
                is_terminal = True
                max_coins_obtainable = coin_counter
                if coin_counter == 0 and right_arrow_index == 0:
                    ## Check if the row only contains '>'. If so, our run is
                    ## forced to end here.
                    is_end = True
                    for cell in row:
                        if cell != '>':
                            is_end = False
                            break
                        
            elif right_arrow_index != -1:
                ## Row contains a right arrow after a down arrow (wrap arround).
                max_coins_obtainable = max(max_coins_obtainable,
                                           coin_counter - coins_before_index[right_arrow_index] + coins_before_index[first_down_index])
                
        else:
            ## Row does not contain a right arrow, so the best we can do is pass
            ## through a single coin on the row if the row has a coin.
            if coin_counter > 0:
                max_coins_obtainable = 1
        
        return max_coins_obtainable, is_terminal, is_end

    stack = []

    ## Process each row. Stop if we come across a row with only right arrows.
    ## Since we cannot reach the rows below, there is no reason to process them.
    for row in G:
        max_coins, is_terminal, is_end = process_row(row)
        stack.append((max_coins, is_terminal))
        if is_end == True:
            break

    ## Iteratively compute the maximum number of coins we can obtain by starting
    ## in each row, starting from the bottom.
    max_coins_collectable = [0] * len(stack)
    while len(stack) > 0:
        max_coin_in_row, is_terminal = stack.pop()
        if is_terminal:
            contains_coin = 1
            if max_coin_in_row == 0:
                contains_coin = 0
            ## Pass current row and get max of remaining rows, or get all the
            ## coins in the current row end run.
            max_coins_collectable.append(max(max_coins_collectable[-1] + contains_coin, max_coin_in_row))
        else:
            max_coins_collectable.append(max_coins_collectable[-1] + max_coin_in_row)

    return max_coins_collectable[-1]

## Test Cases
if __name__ == "__main__":
    ## Test Case 1
    R = 3
    C = 4
    G = [['.', '*', '*', '*'],
         ['*', '*', 'v', '>'],
         ['.', '*', '.', '.']]

    print("Test Case 1")
    print("Expected Return Value = 4")
    print("Actual Return Value   = {}".format(getMaxCollectableCoins(R, C, G)))
    print("")

    ## Test Case 2
    R = 3
    C = 3
    G = [['>', '*', '*'],
         ['*', '>', '*'],
         ['*', '*', '>']]

    print("Test Case 2")
    print("Expected Return Value = 4")
    print("Actual Return Value   = {}".format(getMaxCollectableCoins(R, C, G)))
    print("")

    ## Test Case 3
    R = 2
    C = 2
    G = [['>', '>'],
         ['*', '*']]

    print("Test Case 3")
    print("Expected Return Value = 0")
    print("Actual Return Value   = {}".format(getMaxCollectableCoins(R, C, G)))
    print("")

    ## Test Case 4
    R = 4
    C = 6
    G = [['>', '*', 'v', '*', '>', '*'],
         ['*', 'v', '*', 'v', '>', '*'],
         ['.', '*', '>', '.', '.', '*'],
         ['.', '*', '.', '.', '*', 'v']]

    print("Test Case 4")
    print("Expected Return Value = 6")
    print("Actual Return Value   = {}".format(getMaxCollectableCoins(R, C, G)))
    print("")
