from itertools import permutations

def read_input():
    file = open("Data/day13.txt", "r")
    guests = {}
    
    for line in file:
        line = line.strip(".\n").split()
        guests[(line[0], line[-1])] = int(line[3])
        
        if line[2] == "lose":
            guests[(line[0], line[-1])] *= -1
            
    return guests

def get_guest_list(guests):
    guest_list = set()
    for item in guests.keys():
        guest_list.add(item[0])
        
    return guest_list

def include_me(guests, guest_list):
    for person in guest_list:
        guests[("Me", person)] = 0
        guests[(person, "Me")] = 0
        
    guest_list.add("Me")
    
    return guests, guest_list

def seating_arrangement(guests, guest_list):
    max_happiness = 0
    
    for order in permutations(guest_list):
        happiness = 0
        
        for i in range(len(order)):
            happiness += guests[(order[i], order[(i+1)%len(order)])]
            happiness += guests[(order[(i+1)%len(order)], order[i])]
            
        max_happiness = max(max_happiness, happiness)
        
    return max_happiness
            
if __name__ == "__main__":
    guests = read_input()
    guest_list = get_guest_list(guests)
    print(f"Part one: {seating_arrangement(guests, guest_list)}")
    guests, guest_list = include_me(guests, guest_list)
    print(f"Part two: {seating_arrangement(guests, guest_list)}")
    