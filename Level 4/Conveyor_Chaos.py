from typing import List

class Node:
    def __init__(self, conveyor):
        self.left_coord  = conveyor[0]
        self.right_coord = conveyor[1]
        self.left       = None
        self.right      = None
        self.count      = 0
        self.center     = 0
        self.ceil_count = 0
        self.ceil_center = 0
        self.travel = 0

def create_nodes(conveyors):
    nodes = dict()

    for conveyor in conveyors:
        nodes[conveyor] = Node(conveyor)

    return nodes

def create_tree(conveyors, nodes):
    for i in range(1, len(conveyors)):
        curr = nodes[conveyors[i]]
        
        for j in range(i - 1, -1, -1):
            prev = nodes[conveyors[j]]
            if curr.left_coord > prev.left_coord and curr.left_coord < prev.right_coord:
                curr.left = prev
                break
            
        for j in range(i - 1, -1, -1):
            prev = nodes[conveyors[j]]
            if curr.right_coord > prev.left_coord and curr.right_coord < prev.right_coord:
                curr.right = prev
                break

        if curr.left is None:
            curr.left = nodes[conveyors[0]]
        if curr.right is None:
            curr.right = nodes[conveyors[0]]
            
        curr.travel = (curr.right_coord - curr.left_coord + curr.left.travel + curr.right.travel) / 2
        
def set_probabilities(conveyors, nodes):
    ceiling = [0] * 1000001

    conveyors.reverse()
    
    for conveyor in conveyors:
        curr = nodes[conveyor]
        start = curr.left_coord
        index = start
        count = 0
        center = 0
        
        while index < curr.right_coord:
            if ceiling[index] == 0:
                index += 1
                continue

            span = index - start
            count += span
            center += (index + start) * span
            
            for i in range(start, index):
                ceiling[i] = index

            index = ceiling[index]
            start = index

        span = index - start
        count += span
        center += (index + start) * span

        for i in range(start, index):
            ceiling[i] = index

        if count != 0:
            curr.count = count
            curr.center = center
            curr.ceil_count = count / 1000000
            curr.ceil_center = center / count / 2

    temp = conveyors.pop(-1)
    for conveyor in conveyors:
        curr = nodes[conveyor]
        curr.left.count += curr.count / 2
        curr.left.center += curr.left_coord * curr.count
        curr.right.count += curr.count / 2
        curr.right.center += curr.right_coord * curr.count

    conveyors.append(temp)
    for conveyor in conveyors:
        curr = nodes[conveyor]
        if curr.count != 0:
            curr.center = curr.center / curr.count / 2
            curr.count = curr.count / 1000000

def expected_travel(nodes):
    dist = 0
    for conveyor in nodes:
        node = nodes[conveyor]
        dist += node.travel * node.ceil_count

    return dist

def get_optimal_delta(nodes):
    min_delta = 0

    del nodes[(0, 1000000, 0)]
    for conveyor in nodes:
        node = nodes[conveyor]
        travel = min(node.left.travel + node.center - node.left_coord, node.right.travel + node.right_coord - node.center)
        delta = (travel - node.travel) * node.count

        min_delta = min(min_delta, delta)

    return min_delta

def getMinExpectedHorizontalTravelDistance(N: int, H: List[int], A: List[int], B: List[int]) -> float:
    FLOOR = (0, 1000000, 0)
    conveyors = [FLOOR] + sorted(list(zip(A, B, H)), key = lambda x: x[2])
    
    nodes = create_nodes(conveyors)
    create_tree(conveyors, nodes)
    set_probabilities(conveyors, nodes)
    dist = expected_travel(nodes)
    min_delta = get_optimal_delta(nodes)
    
    return dist + min_delta

if __name__ == '__main__':
    N = 5
    H = [2, 8, 5, 9, 4]
    A = [5000, 2000, 7000, 9000, 0]
    B = [7000, 8000, 11000, 11000, 4000]

    a = getMinExpectedHorizontalTravelDistance(N, H, A, B)

    print(a)
