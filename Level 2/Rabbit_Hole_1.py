## Problem: Rabbit Hole 1
## You're having a grand old time clicking through the rabbit hole that is your
## favorite online encyclopedia.

## The encyclopedia consists of N different web pages, numbered from 1 to N.
## Each page i contains nothing but a single link to a different page L{i}.

## A session spent on this website involves beginning on one of the N pages,
## and then navigating around using the links until you decide to stop. That is,
## while on page i, you may either move to page L{i}, or stop your browsing
## session.

## Assuming you can choose which page you begin the session on, what's the
## maximum number of different pages you can visit in a single session? Note
## that a page only counts once even if visited multiple times during the
## session.

## Constraints:
## 2 <= N <= 500,000
## 1 <= L{i} <= N
## L{i} ≠ i

## Solution
## Time Complexity: O(N)
## Space Complexity: O(N)
## Explanation: This problem is a depth-first seach problem with a few extra
## steps. While we run DFS, we want to keep track of the number of pages we have
## visited from the starting node S and tag each page with the id of the S.
## Eventually we will reach a visited page X that is either part of the current
## DFS chain (tag equals S) or not. If the tag is the same, then we have a
## cycle. Set the maximum number of pages visitable by any page in a cycle C to
## the number of pages in C and set the tag to a negative value. If the tag is
## different, then we go back up the DFS chain setting the maximum visitable
## value at page P to the maximum number of pages L{P} can visit plus one.

from typing import List

def getMaxVisitableWebpages(N: int, L: List[int]) -> int:
    page_id = [0] * (N + 1)
    max_visitable_from_page = [0] * (N + 1)

    ## If page hasn't been visited yet, run DFS starting at page
    for page in range(1, N + 1):
        if page_id[page] != 0:
            continue

        starting_page = page
        pages_visited = 0

        ## DFS until we reach a page that has already been visited.
        ## Set the ID of each page visited to the starting page.
        while page_id[page] == 0:
            pages_visited += 1
            page_id[page] = starting_page
            max_visitable_from_page[page] = pages_visited
            page = L[page - 1]

        ## If the page_id is the same as the starting page, the DFS has looped
        ## back into itself.
        if page_id[page] == starting_page:
            pages_in_cycle = pages_visited - max_visitable_from_page[page] + 1

            ## Set the max_visitable value of each page in the cycle to
            ## pages_in_cycle.
            while page_id[page] != -starting_page:
                page_id[page] = -starting_page
                max_visitable_from_page[page] = pages_in_cycle
                page = L[page - 1]

        ## If the page_id is different from the starting page, the DFS has
        ## reached a page visited in a previous DFS run.
        else:
            pages_visited += max_visitable_from_page[page]

        ## Run DFS again and set the max_visitable value of each page to
        ## pages_visited while decrementing pages_visited for each page visited.
        page = starting_page
        while page_id[page] == starting_page:
            max_visitable_from_page[page] = pages_visited
            pages_visited -= 1
            page = L[page - 1]

    return max(max_visitable_from_page)

## Test Cases
if __name__ == "__main__":
    ## Test Case 1
    N = 4
    L = [4, 1, 2, 1]

    print("Test Case 1")
    print("Expected Return Value = 4")
    print("Actual Return Value   = {}".format(getMaxVisitableWebpages(N, L)))
    print("")

    ## Test Case 2
    N = 5
    L = [4, 3, 5, 1, 2]

    print("Test Case 2")
    print("Expected Return Value = 3")
    print("Actual Return Value   = {}".format(getMaxVisitableWebpages(N, L)))
    print("")

    ## Test Case 3
    N = 5
    L = [2, 4, 2, 2, 3]

    print("Test Case 3")
    print("Expected Return Value = 4")
    print("Actual Return Value   = {}".format(getMaxVisitableWebpages(N, L)))
    print("")
