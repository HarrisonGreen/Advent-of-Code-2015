import json

def read_input():
    file = open("Data/day12.json", "r")
    return json.load(file)

def calculate_sum(accounts):
        
    if type(accounts) == str:
        return 0
    elif type(accounts) == int:
        return accounts
    elif type(accounts) == list:
        return sum(calculate_sum(item) for item in accounts)
    elif type(accounts) == dict:
        return sum(calculate_sum(item) for item in accounts.values())
        
def calculate_sum_no_red(accounts):
    
    if type(accounts) == str:
        return 0
    elif type(accounts) == int:
        return accounts
    elif type(accounts) == list:
        return sum(calculate_sum_no_red(item) for item in accounts)
    elif type(accounts) == dict:
        if "red" in accounts.values():
            return 0
        else:
            return sum(calculate_sum_no_red(item) for item in accounts.values())
    
if __name__ == "__main__":
    accounts = read_input()
    print(f"Part one: {calculate_sum(accounts)}")
    print(f"Part two: {calculate_sum_no_red(accounts)}")
