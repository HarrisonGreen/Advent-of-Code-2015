def read_input():
    file = open("Data/day1.txt", "r")
    for line in file:
        return line
        
def find_floor(instructions):
    print(f"Part one: {instructions.count('(') - instructions.count(')')}")
    
def basement_number(instructions):
    floor = 0
    for i in range(len(instructions)):
        if instructions[i] == "(":
            floor += 1
        else:
            floor -= 1
            
        if floor < 0:
            break
        
    print(f"Part two: {i+1}")
    
if __name__ == "__main__":
    instructions = read_input()
    find_floor(instructions)
    basement_number(instructions)
    