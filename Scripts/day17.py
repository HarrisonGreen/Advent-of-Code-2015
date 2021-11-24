def read_input():
    file = open("Data/day17.txt", "r")
    containers = []
    
    for line in file:
        line = int(line.strip("\n"))
        containers.append(line)
        
    return sorted(containers, reverse = True)

def count_combinations(containers, litres):
    
    if sum(containers) < litres:
        return 0
    
    if containers[0] > litres:
        return count_combinations(containers[1:], litres)

    if containers[0] < litres:
        return (count_combinations(containers[1:], litres) +
                count_combinations(containers[1:], litres - containers[0]))
    
    if containers[0] == litres:
        return 1 + count_combinations(containers[1:], litres)
    
def minimal_combinations(containers, litres, used):
    
    if sum(containers) < litres:
        pass
    
    elif containers[0] > litres:
        minimal_combinations(containers[1:], litres, used)
        
    elif containers[0] < litres:
        minimal_combinations(containers[1:], litres, used)
        minimal_combinations(containers[1:], litres - containers[0], used + 1)
        
    elif containers[0] == litres:
        count[used+1] = count.get(used+1, 0) + 1
        minimal_combinations(containers[1:], litres, used)

if __name__ == "__main__":
    containers = read_input()
    print(f"Part one: {count_combinations(containers, 150)}")
    count = {}
    minimal_combinations(containers, 150, 0)
    print(f"Part two: {count[min(count.keys())]}")
    