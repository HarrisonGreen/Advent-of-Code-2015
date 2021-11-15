def read_input():
    file = open("Data/day5.txt", "r")
    strings = []
    
    for line in file:
        strings.append(line.strip("\n"))
        
    return strings

def count_vowels(string):
    return (string.count("a") + string.count("e") + string.count("i") +
            string.count("o") + string.count("u"))

def double_letter(string):
    for i in range(len(string) - 1):
        if string[i] == string[i+1]:
            return True
        
    return False

def forbidden_strings(string):
    return "ab" in string or "cd" in string or "pq" in string or "xy" in string

def count_strings(strings):
    count = 0
    
    for string in strings:
        if count_vowels(string) < 3:
            continue
        if not double_letter(string):
            continue
        if forbidden_strings(string):
            continue
        
        count += 1
        
    print(f"Part one: {count}")
    
def repeat_pair(string):
    for i in range(len(string) - 3):
        for j in range(i+2, len(string) - 1):
            if string[i:i+2] == string[j:j+2]:
                return True
            
    return False

def repeat_gap(string):
    for i in range(len(string) - 2):
        if string[i] == string[i+2]:
            return True
        
    return False

def new_count_strings(strings):
    count = 0
    
    for string in strings:
        if not repeat_pair(string):
            continue
        if not repeat_gap(string):
            continue
        
        count += 1
        
    print(f"Part two: {count}")
    
if __name__ == "__main__":
    strings = read_input()
    count_strings(strings)
    new_count_strings(strings)
    