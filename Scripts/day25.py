def find_number(r, c):
    d = r + c - 1
    num = d*(d-1)//2 + c
    
    v = 20151125
    for _ in range(num - 1):
        v = (v * 252533)%33554393
    
    print(f"Part one: {v}")
    
if __name__ == "__main__":
    row = 3010
    column = 3019
    find_number(row, column)
    