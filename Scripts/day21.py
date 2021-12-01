from itertools import combinations

def items():
    weapons = {"Dagger": {"Cost": 8, "Damage": 4, "Armour": 0},
               "Shortsword": {"Cost": 10, "Damage": 5, "Armour": 0},
               "Warhammer": {"Cost": 25, "Damage": 6, "Armour": 0},
               "Longsword": {"Cost": 40, "Damage": 7, "Armour": 0},
               "Greataxe": {"Cost": 74, "Damage": 8, "Armour": 0},
               }
    
    armour = {"None": {"Cost": 0, "Damage": 0, "Armour": 0},
              "Leather": {"Cost": 13, "Damage": 0, "Armour": 1},
              "Chainmail": {"Cost": 31, "Damage": 0, "Armour": 2},
              "Splintmail": {"Cost": 53, "Damage": 0, "Armour": 3},
              "Bandedmail": {"Cost": 75, "Damage": 0, "Armour": 4},
              "Platemail": {"Cost": 102, "Damage": 0, "Armour": 5},
              }
    
    rings = {"Left - None": {"Cost": 0, "Damage": 0, "Armour": 0},
             "Right - None": {"Cost": 0, "Damage": 0, "Armour": 0},
             "Damage +1": {"Cost": 25, "Damage": 1, "Armour": 0},
             "Damage +2": {"Cost": 50, "Damage": 2, "Armour": 0},
             "Damage +3": {"Cost": 100, "Damage": 3, "Armour": 0},
             "Defense +1": {"Cost": 20, "Damage": 0, "Armour": 1},
             "Defense +2": {"Cost": 40, "Damage": 0, "Armour": 2},
             "Defense +3": {"Cost": 80, "Damage": 0, "Armour": 3},
             }
    
    return weapons, armour, rings

def battle(me):
    boss = {"HP": 103, "Damage": 9, "Armour": 2}
    
    while True:
        boss["HP"] -= max(1, me["Damage"]-boss["Armour"])
        
        if boss["HP"] <= 0:
            return True
        
        me["HP"] -= max(1, boss["Damage"]-me["Armour"])
        
        if me["HP"] <= 0:
            return False
        
def find_best_items():
    weapons, armour, rings = items()
    min_cost = 10000
    
    for my_weapon in weapons.keys():
        for my_armour in armour.keys():
            for my_rings in combinations(rings.keys(), 2):
                
                me = {"HP": 100, "Damage": 0, "Armour": 0}
                me["Damage"] += weapons[my_weapon]["Damage"]
                me["Armour"] += armour[my_armour]["Armour"]
                me["Damage"] += rings[my_rings[0]]["Damage"]
                me["Armour"] += rings[my_rings[0]]["Armour"]
                me["Damage"] += rings[my_rings[1]]["Damage"]
                me["Armour"] += rings[my_rings[1]]["Armour"]
                
                cost = (weapons[my_weapon]["Cost"] + armour[my_armour]["Cost"] +
                        rings[my_rings[0]]["Cost"] + rings[my_rings[1]]["Cost"])
                
                if battle(me):
                    min_cost = min(cost, min_cost)
                    
    print(f"Part one: {min_cost}")
    
def find_worst_items():
    weapons, armour, rings = items()
    max_cost = 0
    
    for my_weapon in weapons.keys():
        for my_armour in armour.keys():
            for my_rings in combinations(rings.keys(), 2):
                
                me = {"HP": 100, "Damage": 0, "Armour": 0}
                me["Damage"] += weapons[my_weapon]["Damage"]
                me["Armour"] += armour[my_armour]["Armour"]
                me["Damage"] += rings[my_rings[0]]["Damage"]
                me["Armour"] += rings[my_rings[0]]["Armour"]
                me["Damage"] += rings[my_rings[1]]["Damage"]
                me["Armour"] += rings[my_rings[1]]["Armour"]
                
                cost = (weapons[my_weapon]["Cost"] + armour[my_armour]["Cost"] +
                        rings[my_rings[0]]["Cost"] + rings[my_rings[1]]["Cost"])
                
                if not battle(me):
                    max_cost = max(cost, max_cost)
                    
    print(f"Part two: {max_cost}")
                
if __name__ == "__main__":
    find_best_items()
    find_worst_items()
    