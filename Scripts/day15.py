from itertools import combinations
from copy import copy

def read_input():
    file = open("Data/day15.txt", "r")
    ingredients = []
    
    for line in file:
        line = line.split()
        line = (line[0][:-1], int(line[2][:-1]), int(line[4][:-1]),
                int(line[6][:-1]), int(line[8][:-1]), int(line[10]))
        ingredients.append(line)
        
    return ingredients

def score(tsps, ings):
    cap = max(sum(tsps[i]*ings[i][1] for i in range(len(tsps))), 0)
    dur = max(sum(tsps[i]*ings[i][2] for i in range(len(tsps))), 0)
    fla = max(sum(tsps[i]*ings[i][3] for i in range(len(tsps))), 0)
    tex = max(sum(tsps[i]*ings[i][4] for i in range(len(tsps))), 0)
    
    return cap*dur*fla*tex

def optimise_cookie(ingredients):
    tsps = [100//len(ingredients) for _ in range(len(ingredients))]
    old_score = score(tsps, ingredients)
    
    while True:
        old_tsps = copy(tsps)
        
        for pair in combinations(range(len(ingredients)), 2):
            tsps[pair[0]] += 1
            tsps[pair[1]] -= 1
            if score(tsps, ingredients) > old_score:
                old_score = score(tsps, ingredients)
                continue
            else:
                tsps[pair[0]] -= 1
                tsps[pair[1]] += 1
                
            tsps[pair[0]] -= 1
            tsps[pair[1]] += 1
            if score(tsps, ingredients) > old_score:
                old_score = score(tsps, ingredients)
                continue
            else:
                tsps[pair[0]] += 1
                tsps[pair[1]] -= 1
                
        if tsps == old_tsps:
            break
        
    print(f"Part one: {old_score}")
    
def optimise_cookie_calories(ingredients):
    max_score = 0
    
    for a in range(0, 101):
        for b in range(0, 101-a):
            cal = 500 - a*ingredients[0][5] - b*ingredients[1][5]
            tsp = 100 - a - b
            
            c = (cal - ingredients[3][5]*tsp)/(ingredients[2][5] - ingredients[3][5])
            d = tsp - c
            
            if c == int(c):
                max_score = max(score((a,b,c,d), ingredients), max_score)
        
    print(f"Part two: {int(max_score)}")
    
if __name__ == "__main__":
    ingredients = read_input()
    optimise_cookie(ingredients)
    optimise_cookie_calories(ingredients)
    