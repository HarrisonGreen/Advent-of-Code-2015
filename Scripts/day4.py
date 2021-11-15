from hashlib import md5

def adventcoin(key):
    i = 0
    
    while True:
        i += 1
        string = key + str(i)
        result = md5(string.encode()).hexdigest()
        
        if result.startswith("00000"):
            break
        
    print(f"Part one: {i}")
    
def long_adventcoin(key):
    i = 0
    
    while True:
        i += 1
        string = key + str(i)
        result = md5(string.encode()).hexdigest()
        
        if result.startswith("000000"):
            break
        
    print(f"Part two: {i}")
        
if __name__ == "__main__":
    key = "ckczppom"
    adventcoin(key)
    long_adventcoin(key)
    