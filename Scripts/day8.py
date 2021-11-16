def char_difference():
    file = open("Data/day8.txt", "r")
    total = 0

    for line in file:
        line = line.strip("\n")
        total += len(line) - len(eval(line))

    print(f"Part one: {total}")
    
def count_extra_chars():
    file = open("Data/day8.txt", "r")
    total = 0

    for line in file:
        line = line.strip("\n")
        total += 2 + line.count("\"") + line.count("\\")

    print(f"Part two: {total}")
    
if __name__ == "__main__":
    char_difference()
    count_extra_chars()
