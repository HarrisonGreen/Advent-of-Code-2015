def generate_next_sequence(sequence):
    new_sequence = ""
    current_digit = sequence[0]
    count = 0
    
    for i in range(len(sequence)):
        if sequence[i] == current_digit:
            count += 1
        else:
            new_sequence += str(count)
            new_sequence += str(current_digit)
            count = 1
            current_digit = sequence[i]
            
    new_sequence += str(count)
    new_sequence += str(current_digit)
            
    return new_sequence
            
def look_and_say(sequence):
    for i in range(40):
        sequence = generate_next_sequence(sequence)
        
    print(f"Part one: {len(sequence)}")
    
    for i in range(10):
        sequence = generate_next_sequence(sequence)
        
    print(f"Part two: {len(sequence)}")
    
if __name__ == "__main__":
    sequence = "1113122113"
    look_and_say(sequence)
    