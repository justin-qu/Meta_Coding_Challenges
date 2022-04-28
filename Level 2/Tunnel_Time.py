## Problem: Tunnel Time
## There’s a circular train track with a circumference of C metres. Positions
## along the track are measured in metres, clockwise from its topmost point. For
## example, the topmost point is position 0, 1 metre clockwise along the track
## is position 1, and 1 metre counterclockwise along the track is position
## C - 1.

## A train with negligible length runs clockwise along this track at a speed of
## 1 metre per second, starting from position 0. After C seconds go by, the
## train will have driven around the entire track and returned to position 0, at
## which point it will continue going around again, with this process repeated
## indefinitely.

## There are N tunnels covering sections of the track, the ith of which begin
## at position A{i} and ends at position B{i} (and therefore has a length of
## B{i} - A{i} metres). No tunnel covers or touches position 0 (including at
## its endpoints), and no two tunnels intersect or touch one another (including
## at their endpoints). For example, if there's a tunnel spanning the interval
## of positions [1, 4], there cannot be another tunnel spanning intervals [2, 3]
## nor [4, 5].

## The train’s tunnel time is the total number of seconds it has spent going
## through tunnels so far. Determine the total number of seconds which will go
## by before the train’s tunnel time becomes K.

## Constraints:
## 3 <= C <= 10^(12)
## 1 <= N <= 500,000
## 1 <= A{i} < B{i} <= C - 1
## 1 <= K <= 10^(12)
## 1 <= getSecondsElapsed(C, N, A, B) <= 10^(15)

## Solution
## Time Complexity: O(N * log(N))
## Space Complexity: O(N), O(1) if sorting done in-place.
## Explanation: In O(N) time, we can calculate the total length of tunnels on
## the track. Using this, we can compute the number of laps around the track
## the train must travel and the remaining tunnel time needed on the final lap.
## Then iterate through the tunnels and accummulate the time spent in a tunnel
## until it reaches K. To facilitate this, we sort A and B in O(N * log(N))
## time.

from typing import List

def getSecondsElapsed(C: int, N: int, A: List[int], B: List[int], K: int) -> int:
    ## Compute number of full laps needed and remaining tunnel time
    laps, K = divmod(K, sum(B) - sum(A))
    seconds_elapsed = laps * C

    a = sorted(A)
    b = sorted(B)
    
    ## If remaining tunnel time is exactly 0, we can end at the end of the final
    if K == 0:
        return seconds_elapsed - C + b[-1]

    ## Add lengths of tunnels until accumulated tunnel time becomes greater than
    ## the target tunnel time
    tunnel_time = 0
    for i in range(N):
        tunnel_start = a[i]
        tunnel_end   = b[i]
        tunnel_length = tunnel_end - tunnel_start

        tunnel_time += tunnel_length

        if tunnel_time >= K:
            return seconds_elapsed + tunnel_end - (tunnel_time - K)

## Test Cases
if __name__ == "__main__":
    ## Test Case 1
    C = 10
    N = 2
    A = [1, 6]
    B = [3, 7]
    K = 7

    print("Test Case 1")
    print("Expected Return Value = 22")
    print("Actual Return Value   = {}".format(getSecondsElapsed(C, N, A, B, K)))
    print("")

    ## Test Case 2
    C = 50
    N = 3
    A = [39, 19, 28]
    B = [49, 27, 35]
    K = 15

    print("Test Case 2")
    print("Expected Return Value = 35")
    print("Actual Return Value   = {}".format(getSecondsElapsed(C, N, A, B, K)))
    print("")
