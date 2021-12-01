def read_input():
    file = open("Data/day23.txt", "r")
    instructions = []
    
    for line in file:
        line = line.strip("\n").replace(",", "").split()
        
        if line[0] == "jmp":
            line[1] = int(line[1])
        elif line[0] in ("jie", "jio"):
            line[2] = int(line[2])
            
        instructions.append(line)
        
    return instructions

def run_program(instructions, registers):
    pos = 0
    
    while pos < len(instructions):
        instruction = instructions[pos]
        
        if instruction[0] == "hlf":
            registers[instruction[1]] //= 2
            pos += 1
        elif instruction[0] == "tpl":
            registers[instruction[1]] *= 3
            pos += 1
        elif instruction[0] == "inc":
            registers[instruction[1]] += 1
            pos += 1
        elif instruction[0] == "jmp":
            pos += instruction[1]
        elif instruction[0] == "jie":
            if registers[instruction[1]]%2 == 0:
                pos += instruction[2]
            else:
                pos += 1
        elif instruction[0] == "jio":
            if registers[instruction[1]] == 1:
                pos += instruction[2]
            else:
                pos += 1
                
    return registers["b"]
    
if __name__ == "__main__":
    instructions = read_input()
    print(f"Part one: {run_program(instructions, {'a': 0, 'b': 0})}")
    print(f"Part two: {run_program(instructions, {'a': 1, 'b': 0})}")
    