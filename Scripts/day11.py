def increment_password(password):
    pos = len(password)

    while True:
        pos -= 1

        if password[pos] == "z":
            password = password[:pos] + "a" + password[pos+1:]
        else:
            password = password[:pos] + chr(ord(password[pos])+1) + password[pos+1:]
            break

    return password

def remove_iol(password):
    for i in range(len(password)):
        if password[i] == "i":
            password = password[:i] + "j" + password[i+1:]
        elif password[i] == "o":
            password = password[:i] + "p" + password[i+1:]
        elif password[i] == "l":
            password = password[:i] + "m" + password[i+1:]

    return password

def streak_check(password):
    for i in range(len(password)-2):
        if ord(password[i]) == ord(password[i+1]) - 1:
            if ord(password[i]) == ord(password[i+2]) - 2:
                return True
    
    return False

def pair_check(password):
    letters = set()
    
    for i in range(len(password)-1):
        if password[i] == password[i+1]:
            letters.add(password[i])

    return len(letters) > 1

def find_password(password):
    while True:
        old_password = password

        if not streak_check(password):
            password = increment_password(password)

        if not pair_check(password):
            password = increment_password(password)

        password = remove_iol(password)
        if password == old_password:
            return password
    
if __name__ == "__main__":
    password = "hxbxwxba"
    password = find_password(password)
    print(f"Part one: {password}")
    password = find_password(increment_password(password))
    print(f"Part Two: {password}")
