from copy import copy

def advance_turn(me, boss, spent, shield, poison, recharge, move, diff="medium"):
    
    me, boss, spent, shield, poison, recharge, move = (copy(me), copy(boss),
    copy(spent), copy(shield), copy(poison), copy(recharge), copy(move))
    
    # Player move
    if move == 0:
        if me["mana"] < 53:
            return (me, boss, spent, shield, poison, recharge, -1)
        
        spent += 53
        me["mana"] -=  53
        boss["hp"] -= 4
        if boss["hp"] <= 0:
            return (me, boss, spent, shield, poison, recharge, 1)
        
    elif move == 1:
        if me["mana"] < 73:
            return (me, boss, spent, shield, poison, recharge, -1)
        
        spent += 73
        me["mana"] -= 73
        boss["hp"] -= 2
        me["hp"] += 2
        if boss["hp"] <= 0:
            return (me, boss, spent, shield, poison, recharge, 1)
        
    elif move == 2:
        if me["mana"] < 113:
            return (me, boss, spent, shield, poison, recharge, -1)
        if shield > 0:
            return (me, boss, spent, shield, poison, recharge, -1)
        
        spent += 113
        me["mana"] -= 113
        me["armour"] = 7
        shield = 6
        
    elif move == 3:
        if me["mana"] < 173:
            return (me, boss, spent, shield, poison, recharge, -1)
        if poison > 0:
            return (me, boss, spent, shield, poison, recharge, -1)
        
        spent += 173
        me["mana"] -= 173
        poison = 6
        
    elif move == 4:
        if me["mana"] < 229:
            return (me, boss, spent, shield, poison, recharge, -1)
        if recharge > 0:
            return (me, boss, spent, shield, poison, recharge, -1)
        
        spent += 229
        me["mana"] -= 229
        recharge = 5
        
    # Start of boss' turn
    if shield > 0:
        shield -= 1
        if shield == 0:
            me["armour"] = 0
        
    if poison > 0:
        poison -= 1
        boss["hp"] -= 3
        if boss["hp"] <= 0:
            return (me, boss, spent, shield, poison, recharge, 1)
        
    if recharge > 0:
        recharge -= 1
        me["mana"] += 101
        
    # Boss attacks
    me["hp"] -= max(1, boss["damage"]-me["armour"])
    
    if me["hp"] <= 0:
        return (me, boss, spent, shield, poison, recharge, -1)
    
    # Start of player's turn
    if diff == "hard":
        me["hp"] -= 1
        if me["hp"] <= 0:
            return (me, boss, spent, shield, poison, recharge, -1)
    
    if shield > 0:
        shield -= 1
        if shield == 0:
            me["armour"] = 0
        
    if poison > 0:
        poison -= 1
        boss["hp"] -= 3
        if boss["hp"] <= 0:
            return (me, boss, spent, shield, poison, recharge, 1)
        
    if recharge > 0:
        recharge -= 1
        me["mana"] += 101
        
    return (me, boss, spent, shield, poison, recharge, 0)

def find_least_mana(diff):
    me = {"hp": 50, "mana": 500, "armour": 0}
    boss = {"hp": 51, "damage": 9}
    if diff == "hard":
        me["hp"] -= 1
    least_mana = 1000000
    states = [(me, boss, 0, 0, 0, 0)]
    
    while states:
        s = states.pop(0)
        
        if s[2] >= least_mana:
            continue
        
        for move in range(5):
            new = advance_turn(s[0], s[1], s[2], s[3], s[4], s[5], move, diff)
            
            if new[6] == -1:
                pass
            elif new[6] == 1:
                least_mana = min(new[2], least_mana)
            elif new[2] < least_mana:
                states.append(new)
                
    return least_mana
    
if __name__ == "__main__":
    print(f"Part one: {find_least_mana('medium')}")
    print(f"Part two: {find_least_mana('hard')}")
    