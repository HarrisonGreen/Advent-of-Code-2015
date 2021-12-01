def read_input():
    file = open("Data/day24.txt", "r")
    packages = []
    
    for line in file:
        packages.append(int(line.strip("\n")))
        
    return sorted(packages, reverse = True)
    
def find_grouping(packages, target, num, qe):
    
    if sum(packages) < target:
        return False, 0, 0
    
    if packages[0] > target:
        return find_grouping(packages[1:], target, num, qe)
    
    if packages[0] < target:
        include = find_grouping(packages[1:], target-packages[0], num+1, qe*packages[0])
        exclude = find_grouping(packages[1:], target, num, qe)
        
        if include[0] + exclude[0] == 0:
            return False, 0, 0
        elif not include[0]:
            return exclude
        elif not exclude[0]:
            return include
        elif include[1] < exclude[1]:
            return include
        elif exclude[1] < include[1]:
            return exclude
        else:
            return True, include[1], min(include[2], exclude[2])
        
    if packages[0] == target:
        return True, num+1, qe*packages[0]
    
if __name__ == "__main__":
    packages = read_input()
    print(f"Part one: {find_grouping(packages, sum(packages)//3, 0, 1)[2]}")
    print(f"Part two: {find_grouping(packages, sum(packages)//4, 0, 1)[2]}")
    