def read_input():
    file = open("Data/day2.txt", "r")
    presents = []
    
    for line in file:
        presents.append(sorted(list(map(int, line.strip("\n").split("x")))))
        
    return presents

def wrapping_paper(presents):
    total = 0
    
    for present in presents:
        total += 3*present[0]*present[1]
        total += 2*present[0]*present[2]
        total += 2*present[1]*present[2]
        
    print(f"Part one: {total}")
    
def ribbon(presents):
    total = 0
    
    for present in presents:
        total += 2*(present[0]+present[1])
        total += present[0]*present[1]*present[2]
        
    print(f"Part two: {total}")
    
if __name__ == "__main__":
    presents = read_input()
    wrapping_paper(presents)
    ribbon(presents)
    