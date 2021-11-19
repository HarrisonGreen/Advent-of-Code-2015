from itertools import permutations

def read_input():
    file = open("Data/day9.txt", "r")
    distances = {}
    
    for line in file:
        line = line.strip("\n").split(" = ")
        line[0] = line[0].split(" to ")
        distances[(line[0][0], line[0][1])] = int(line[1])
        distances[(line[0][1], line[0][0])] = int(line[1])
        
    return distances

def get_locations(distances):
    locations = set()
    for item in distances.keys():
        locations.add(item[0])
        
    return locations

def shortest_and_longest_routes(distances, locations):
    min_dist = 100000
    max_dist = 0
    
    for order in permutations(locations):
        length = 0
        
        for i in range(len(order)-1):
            length += distances[(order[i], order[i+1])]
            
        min_dist = min(min_dist, length)
        max_dist = max(max_dist, length)
    
    print(f"Part one: {min_dist}")
    print(f"Part two: {max_dist}")
    
if __name__ == "__main__":
    distances = read_input()
    locations = get_locations(distances)
    shortest_and_longest_routes(distances, locations)
