def read_input():
    file = open("Data/day3.txt", "r")
    for line in file:
        return line
    
def count_houses(instructions):
    houses = {(0, 0)}
    x, y = 0, 0
    
    for instruction in instructions:
        if instruction == "^":
            y += 1
        elif instruction == "v":
            y -= 1
        elif instruction == ">":
            x += 1
        elif instruction == "<":
            x -= 1
            
        houses.add((x,y))
        
    print(f"Part one: {len(houses)}")
    
def two_santas(instructions):
    houses = {(0, 0)}
    x, y = [0, 0], [0, 0]
    
    for i in range(len(instructions)):
        if instructions[i] == "^":
            y[i%2] += 1
        elif instructions[i] == "v":
            y[i%2] -= 1
        elif instructions[i] == ">":
            x[i%2] += 1
        elif instructions[i] == "<":
            x[i%2] -= 1
            
        houses.add((x[i%2], y[i%2]))
        
    print(f"Part two: {len(houses)}")
    
if __name__ == "__main__":
    instructions = read_input()
    count_houses(instructions)
    two_santas(instructions)
    