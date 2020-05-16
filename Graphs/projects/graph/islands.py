from util import Stack


islands = [[0,1,0,1,0],
           [1,1,0,1,1],
           [0,0,1,0,0],
           [1,0,1,0,0],
           [1,1,0,0,0]]

# Visit each cell in the 2D array
# When you come across a 1, traverse it and 
# mark all connected nodes as visited
# then increment the counter


def get_island_neighbors(x, y, matrix):
    # Check N,S,E,W don't forget boundaries
    neighbors = []
    # North
    if y > 0 and matrix[y-1][x] == 1:
        neighbors.append((x,y-1))
    # South
    if (y < len(matrix)-1) and matrix[y+1][x] == 1:
        neighbors.append((x,y-1))
    # East
    if x < len(matrix[0])-1 and matrix[y][x+1] == 1:
        neighbors.append((x+1,y))
    # West
    if x > 0 and matrix[y][x-1] == 1:
        neighbors.append((x-1, y))

    return neighbors


def dft_islands(start_x, start_y, matrix, visited):
    '''
    Returns updated visited matrix after a
    dft of matrix starting from x,y
    '''
    s = Stack()
    s.push((start_x,start_y))
    visited = set()

    while s.size() > 0:
        v = s.pop()
        x = v[0]
        y = v[1]

        if not visited[y][x]:
            visited[y][x] = True
            for neighbor in get_island_neighbors(x, y, matrix):
                s.push(neighbor)
    return visited


def island_counter(matrix):
    # Create a visited matrix with the same dims as `islands`
    visited = []
    matrix_height = len(matrix)
    matrix_width = len(matrix[0])
    for i in range(matrix_height):
        visited.append([False] * matrix_width)
    # Create a counter, init to 0
    counter = 0
    # For each cell in 2D array
    for x in range(matrix_width):
        for y in range(matrix_height):
            if not visited[y][x]:
                # If cell not visited yet
                if matrix[y][x] == 1:
                    # DFT it and mark all connected nodes as visited
                    visited = dft_islands(x, y, matrix, visited)
                    # Then increment counter
                    counter += 1
    return counter

if __name__ == "__main__":
    print(island_counter(islands))