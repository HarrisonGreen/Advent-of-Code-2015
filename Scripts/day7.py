def read_input():
    file = open("Data/day7.txt", "r")
    instructions = []
    
    for line in file:
        line = line.strip("\n").split(" -> ")
        
        if "RSHIFT" in line[0]:
            line[0] = line[0].split(" RSHIFT ")
            line = [0, line[0][0], line[0][1], line[1]]
        elif "LSHIFT" in line[0]:
            line[0] = line[0].split(" LSHIFT ")
            line = [1, line[0][0], line[0][1], line[1]]
        elif "AND" in line[0]:
            line[0] = line[0].split(" AND ")
            line = [2, line[0][0], line[0][1], line[1]]
        elif "OR" in line[0]:
            line[0] = line[0].split(" OR ")
            line = [3, line[0][0], line[0][1], line[1]]
        elif "NOT" in line[0]:
            line[0] = line[0].strip(" NOT ")
            line = [4, line[0], 0, line[1]]
        else:
            line = [5, line[0], 0, line[1]]
        
        instructions.append(line)
        
    return instructions

def override_b(instructions, value):
    for i in range(len(instructions)):
        if instructions[i][3] == "b":
            instructions[i][1] = value
            
    return instructions

def assemble_circuit(instructions):
    wires = {}
    
    for i in range(len(instructions)):
        for j in range(1, 3):
            try:
                instructions[i][j] = int(instructions[i][j])
            except ValueError:
                pass
    
    while instructions:
        to_process = []
        
        for i in range(len(instructions)):
            for j in range(1, 3):
                if instructions[i][j] in wires.keys():
                    instructions[i][j] = wires[instructions[i][j]]
                    
            if type(instructions[i][1]) == int and type(instructions[i][2]) == int:
                to_process.append(instructions[i])
                
        for instruction in to_process:
            
            if instruction[0] == 0:
                wires[instruction[3]] = instruction[1] >> instruction[2]
            elif instruction[0] == 1:
                wires[instruction[3]] = instruction[1] << instruction[2]
            elif instruction[0] == 2:
                wires[instruction[3]] = instruction[1] & instruction[2]
            elif instruction[0] == 3:
                wires[instruction[3]] = instruction[1] | instruction[2]
            elif instruction[0] == 4:
                wires[instruction[3]] = 65535 - instruction[1]
            elif instruction[0] == 5:
                wires[instruction[3]] = instruction[1]
                
            instructions.remove(instruction)
            
    return wires["a"]   

if __name__ == "__main__":
    instructions = read_input()
    signal = assemble_circuit(instructions)
    print(f"Part one: {signal}")
    
    instructions = read_input()
    instructions = override_b(instructions, signal)
    signal = assemble_circuit(instructions)
    print(f"Part two: {signal}")
    