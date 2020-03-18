# Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:
from util import Stack

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0],
           [0, 0, 0, 0, 0]]

# island_counter(islands) # returns 4


# Translate the problem into terminology you've learned this week
# Build your graph
# Traverse your graph

def island_counter(matrix):
    # Create a visited matrix
    visited = []
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))
        # for all nodes:
    island_count = 0
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            # if node is not visited:
            if not visited[row][col]:
                if matrix[row][col] == 1:
                    # if we hit a 1 that has not been visited
                    # mark visited
                    visited = dft(row, col, matrix, visited)
                    island_count += 1
        # increment visited count
        # traverse all connected nodes, marking as visited
    return island_count


def dft(start_row, start_col, matrix, visited):
    # Do a DF traversal
    # Return an updated visited matrix will all connected components marked as visited
    # Create a Stack
    s = Stack()
    # push the starting vertex
    s.push((start_row, start_col))
    # Create a set to store visited vertices
    # While the stack is not empty..
    while s.size() > 0:
        # pop the first vertex
        v = s.pop()
        row = v[0]
        col = v[1]
    # Check is it's been visited
        if not visited[row][col]:
            visited[row][col] = True
            for neighbor in get_neighbors(row, col, matrix):
                s.push(neighbor)
    # If it hasn't been visited
    # Mark it as visited
    # push all it's neighbors
    return visited


def get_neighbors(row, col, matrix):
    '''
    Return a list of neighboring 1 tuples in the form [(row, col)]
    '''
    neighbors = []
    # Check north
    if row > 0 and matrix[row-1][col] == 1:
        neighbors.append((row-1, col))
    # Check south
    if row < len(matrix) - 1 and matrix[row+1][col] == 1:
        neighbors.append((row+1, col))
    # Check east
    if col < len(matrix[0]) - 1 and matrix[row][col+1] == 1:
        neighbors.append((row, col+1))
    # Check west
    if col > 0 and matrix[row][col-1] == 1:
        neighbors.append((row, col-1))
    return neighbors


islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
           [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
           [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
           [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
           [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
           [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
           [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
           [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]


print(island_counter(islands))
