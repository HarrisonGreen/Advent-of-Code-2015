import numpy as np

def read_input():
    file = open("Data/day18.txt", "r")
    grid = np.zeros([100,100], dtype=int)
    
    for row, line in enumerate(file):
        line = line.strip("\n")
        
        for column, char in enumerate(line):
            if char == "#":
                grid[row, column] = 1
                
    return grid

def animate_grid(grid):
    for t in range(100):
        to_change = []
        
        for x in range(100):
            for y in range(100):
                neighbours = get_neighbours(x, y)
                count = sum(grid[neighbour] for neighbour in neighbours)
                
                if grid[x, y] == 0 and count == 3:
                    to_change.append((x, y))
                elif grid[x, y] == 1 and count not in (2, 3):
                    to_change.append((x, y))
                    
        for light in to_change:
            grid[light] = 1 - grid[light]
            
    print(f"Part one: {sum(sum(grid))}")
    
def animate_grid_corners_on(grid):
    grid[0, 0] = 1
    grid[0, 99] = 1
    grid[99, 0] = 1
    grid[99, 99] = 1
    
    for t in range(100):
        to_change = []
        
        for x in range(100):
            for y in range(100):
                
                if x in (0, 99) and y in (0, 99):
                    continue
                
                neighbours = get_neighbours(x, y)
                count = sum(grid[neighbour] for neighbour in neighbours)
                
                if grid[x, y] == 0 and count == 3:
                    to_change.append((x, y))
                elif grid[x, y] == 1 and count not in (2, 3):
                    to_change.append((x, y))
                    
        for light in to_change:
            grid[light] = 1 - grid[light]
            
    print(f"Part two: {sum(sum(grid))}")
                
                
def get_neighbours(x, y):
    neighbours = []
    if x < 99:
        neighbours.append((x+1, y))
    if x > 0:
        neighbours.append((x-1, y))
    if y < 99:
        neighbours.append((x, y+1))
    if y > 0:
        neighbours.append((x, y-1))
    if x > 0 and y > 0:
        neighbours.append((x-1, y-1))
    if x > 0 and y < 99:
        neighbours.append((x-1, y+1))
    if x < 99 and y > 0:
        neighbours.append((x+1, y-1))
    if x < 99 and y < 99:
        neighbours.append((x+1, y+1))
        
    return neighbours
    
if __name__ == "__main__":
    grid = read_input()
    animate_grid(grid)
    grid = read_input()
    animate_grid_corners_on(grid)
    