def read_input():
    file = open("Data/day14.txt", "r")
    reindeer = []
    
    for line in file:
        line = line.split()
        line = (line[0], int(line[3]), int(line[6]), int(line[13]))
        reindeer.append(line)
        
    return reindeer

def calculate_distance(reindeer, time):
    max_dist = 0
    
    for deer in reindeer:
        reps = time//(deer[2]+deer[3])
        remainder = time%(deer[2]+deer[3])
        
        dist = deer[1]*deer[2]*reps
        dist += deer[1]*min(deer[2], remainder)
        
        max_dist = max(dist, max_dist)
        
    print(f"Part one: {max_dist}")
    
def calculate_points(reindeer, time):
    points = {deer[0]: 0 for deer in reindeer}
    dist = {deer[0]: 0 for deer in reindeer}
    
    for t in range(time):
        for deer in reindeer:
            
            if t%(deer[2]+deer[3]) < deer[2]:
                dist[deer[0]] += deer[1]
                
        for deer in reindeer:
            if dist[deer[0]] == max(dist.values()):
                points[deer[0]] += 1
                
    print(f"Part two: {max(points.values())}")
    
if __name__ == "__main__":
    reindeer = read_input()
    time = 2503
    calculate_distance(reindeer, time)
    calculate_points(reindeer, time)
    