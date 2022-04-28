## Problem: Rabbit Hole 2
## You're having a grand old time clicking through the rabbit hole that is your
## favorite online encyclopedia.

## The encyclopedia consists of N different web pages, numbered from 1 to N.
## There are M links present across the pages, the ith of which is present on
## page A{i} and links to a different page B{i}. A page may include multiple
## links, including multiple leading to the same other page.

## A session spent on this website involves beginning on one of the N pages,
## and then navigating around using the links until you decide to stop. That is,
## while on page i, you may either move to any of the pages linked to from it,
## or stop your browsing session.

## Assuming you can choose which page you begin the session on, what's the
## maximum number of different pages you can visit in a single session? Note
## that a page only counts once even if visited multiple times during the
## session.

## Constraints:
## 2 <= N <= 500,000
## 1 <= M <= 500,000
## 1 <= A, B <= N
## A{i} ≠ B{i}

## Solution
## Time Complexity: O(N + M)
## Space Complexity: O(N + M)
## Explanation: We use Tarjan's Strongly Connected Components algorithm to find
## strongly connected components and simplify the graph. Tarjan's Algorithm also
## happens to sort the graph in reverse topological order which we can take
## advantage of when computing the maximum visitable pages.

from typing import List

def getMaxVisitableWebpages(N: int, M: int, A: List[int], B: List[int]) -> int:
    scc_id = 1
    page_id = [0] * (N + 1)
    page_cluster_id = [0] * (N + 1)
    max_visitable_from_page = [0] * (N + 1)

    stack        = []
    page_history = []

    links = [set() for _ in range(N + 1)]
    unvisited_links = []

    ## Create adjacency list
    for i in range(M):
        links[A[i]].add(B[i])

    ## Copy of adjacency lists.
    for i in range(N + 1):
        unvisited_links.append(list(links[i]))

    
    for page in range(1, N + 1):
        ## Skip if node already visited
        if page_id[page] != 0:
            continue

        ## Non-recursive Tarjan's SCC Algorithm
        stack.append(page)
        while len(stack) > 0:
            current_page = stack.pop()
            recurse = False

            ## First time seeing current_page
            if current_page > 0:
                page_id[current_page] = scc_id
                page_cluster_id[current_page] = scc_id
                scc_id += 1

                page_history.append(current_page)
                
                avalible_links = unvisited_links[current_page]
                while len(avalible_links) > 0:
                    next_page = avalible_links[-1]
                    if page_id[next_page] == 0:
                        ## Recursivly execute on next_page
                        stack.append(-current_page)
                        stack.append(next_page)
                        recurse = True
                        break

                    if page_id[next_page] > 0:
                        page_cluster_id[current_page] = min(page_cluster_id[current_page], page_id[next_page])

                    del avalible_links[-1]
                    
            ## Continue executing where we left off
            else:
                current_page = -current_page
                avalible_links = unvisited_links[current_page]
                next_page = avalible_links[-1]

                page_cluster_id[current_page] = min(page_cluster_id[current_page], page_cluster_id[next_page])
                del avalible_links[-1]

                while len(avalible_links) > 0:
                    next_page = avalible_links[-1]
                    if page_id[next_page] == 0:
                        ## Recursivly execute on next_page
                        stack.append(-current_page)
                        stack.append(next_page)
                        recurse = True
                        break

                    if page_id[next_page] > 0:
                        page_cluster_id[current_page] = min(page_cluster_id[current_page], page_id[next_page])

                    del avalible_links[-1]

            if recurse == True:
                continue

            ## A Strongly Connected Component Identified
            if page_cluster_id[current_page] == page_id[current_page]:
                prev_page = page_history.pop()
                page_id[prev_page] *= -page_id[current_page]
                scc = [prev_page]
                scc_size = 1

                while prev_page != current_page:
                    prev_page = page_history.pop()
                    page_id[prev_page] *= -page_id[current_page]
                    scc.append(prev_page)
                    scc_size += 1

                ## Condense SCC into a single "page" with union of all links
                scc_links = set()
                for page in scc:
                    scc_links.update(links[page])

                ## Remove links to pages within the SCC
                scc_links.difference_update(scc)

                ## The max visitable from this SCC is 
                max_visitable_from_this_scc = scc_size + max([0] + [max_visitable_from_page[page] for page in scc_links])

                ## Assign the max_visitable value to all pages in the SCC
                for page in scc:
                    max_visitable_from_page[page] = max_visitable_from_this_scc

    return max(max_visitable_from_page)

## Test Cases
if __name__ == "__main__":
    ## Test Case 1
    N = 4
    M = 4
    A = [1, 2, 3, 4]
    B = [4, 1, 2, 1]

    print("Test Case 1")
    print("Expected Return Value = 4")
    print("Actual Return Value   = {}".format(getMaxVisitableWebpages(N, M, A, B)))
    print("")

    ## Test Case 2
    N = 5
    M = 6
    A = [3, 5, 3, 1, 3, 2]
    B = [2, 1, 2, 4, 5, 4]

    print("Test Case 2")
    print("Expected Return Value = 4")
    print("Actual Return Value   = {}".format(getMaxVisitableWebpages(N, M, A, B)))
    print("")

    ## Test Case 3
    N = 10
    M = 9
    A = [3, 2, 5, 9, 10, 3, 3, 9, 4]
    B = [9, 5, 7, 8, 6, 4, 5, 3, 9]
    
    print("Test Case 3")
    print("Expected Return Value = 5")
    print("Actual Return Value   = {}".format(getMaxVisitableWebpages(N, M, A, B)))
    print("")
