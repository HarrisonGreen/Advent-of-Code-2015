def read_input():
    file = open("Data/day16.txt", "r")
    aunts = {}
    
    for line in file:
        line = line.strip("\n").replace(":", "").replace(",", "").split()
        aunts[int(line[1])] = {line[2*i]: int(line[2*i+1]) for i in range(1, len(line)//2)}
        
    return aunts

def find_aunt(aunts, compounds):
    
    for aunt, items in aunts.items():
        correct = 0
        
        for item, number in items.items():
            if number != compounds[item]:
                break
            else:
                correct += 1
        
        if correct == len(items):
            print(f"Part one: {aunt}")
            
def find_aunt_ranges(aunts, compounds):
    
    for aunt, items in aunts.items():
        correct = 0
        
        for item, number in items.items():
            
            if item == "cats" or item == "trees":
                if number > compounds[item]:
                    correct += 1
                else:
                    break
                
            elif item == "pomeranians" or item == "goldfish":
                if number < compounds[item]:
                    correct += 1
                else:
                    break
                
            else:
                if number == compounds[item]:
                    correct += 1
                else:
                    break
        
        if correct == len(items):
            print(f"Part two: {aunt}")
        
    
if __name__ == "__main__":
    aunts = read_input()
    compounds = {"children": 3,
                 "cats": 7,
                 "samoyeds": 2,
                 "pomeranians": 3,
                 "akitas": 0,
                 "vizslas": 0,
                 "goldfish": 5,
                 "trees": 3,
                 "cars": 2,
                 "perfumes": 1}
    find_aunt(aunts, compounds)
    find_aunt_ranges(aunts, compounds)
    