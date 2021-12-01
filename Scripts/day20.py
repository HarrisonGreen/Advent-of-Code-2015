from sympy.ntheory import factorint
import numpy as np

def lowest_house_num(num, step):
    house = 0
    
    while True:
        house += step
        factorisation = factorint(house)
        factors = np.ones(1, dtype=int)
        
        for prime, power in factorisation.items():
            factors = np.outer(np.array([prime**k for k in range(power+1)]), factors).ravel()
            
        if sum(factors)*10 >= num:
            return house
        
def lowest_house_lazy_elves(num, step):
    house = 0
    
    while True:
        house += step
        factors = []
        
        for i in range(1, 51):
            if house/i == house//i:
                factors.append(house//i)
            
        if sum(factors)*11 >= num:
            return house

if __name__ == "__main__":
    step = 2520
    num = 34000000
    print(f"Part one: {lowest_house_num(num, step)}")
    print(f"Part two: {lowest_house_lazy_elves(num, step)}")
    