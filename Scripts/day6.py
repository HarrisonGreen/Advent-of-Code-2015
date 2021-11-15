import numpy as np

def read_input():
    file = open("Data/day6.txt", "r")
    instructions = []
    
    for line in file:
        line = line.strip("\n")
        
        if line.startswith("turn on"):
            line = [0, line.strip("turn on ")]
        elif line.startswith("turn off"):
            line = [1, line.strip("turn off ")]
        elif line.startswith("toggle"):
            line = [2, line.strip("toggle ")]
            
        line[1] = line[1].split(" through ")
        line[1][0] = line[1][0].split(",")
        line[1][1] = line[1][1].split(",")
        
        line = [line[0], line[1][0][0], line[1][0][1], line[1][1][0], line[1][1][1]]
        line = list(map(int, line))
            
        instructions.append(line)
        
    return instructions

def lights(instructions):
    light_grid = np.zeros([1000,1000], dtype=int)
    
    for instr in instructions:
        if instr[0] == 0:
            light_grid[instr[1]:instr[3]+1, instr[2]:instr[4]+1] = 1
        elif instr[0] == 1:
            light_grid[instr[1]:instr[3]+1, instr[2]:instr[4]+1] = 0
        elif instr[0] == 2:
            light_grid[instr[1]:instr[3]+1, instr[2]:instr[4]+1] = (
                1 - light_grid[instr[1]:instr[3]+1, instr[2]:instr[4]+1])
            
    print(f"Part one: {sum(sum(light_grid))}")
    
def new_lights(instructions):
    light_grid = np.zeros([1000,1000], dtype=int)
    
    for instr in instructions:
        if instr[0] == 0:
            light_grid[instr[1]:instr[3]+1, instr[2]:instr[4]+1] += 1
        elif instr[0] == 1:
            light_grid[instr[1]:instr[3]+1, instr[2]:instr[4]+1] -= 1
            light_grid[light_grid < 0] = 0
        elif instr[0] == 2:
            light_grid[instr[1]:instr[3]+1, instr[2]:instr[4]+1] += 2
            
    print(f"Part two: {sum(sum(light_grid))}")
    
if __name__ == "__main__":
    instructions = read_input()
    lights(instructions)
    new_lights(instructions)
    