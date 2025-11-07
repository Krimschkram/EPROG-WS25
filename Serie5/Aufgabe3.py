letters = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,
"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,
"M": 13, "N": 14, "O": 15, "P": 16,"Q": 17,
"R": 18,"S": 19,"T": 20,
"U":21, "V":22, "W": 23, "X": 24,
"Y": 25, "Z": 26}

numbers_to_letters = {v: k for k, v in letters.items()}

def encrypt(m):
    s = ""
    for char in m:
        current_pos = letters[char]
        new_pos = current_pos + 1
        if new_pos not in numbers_to_letters:
            new_pos = 1

        s += numbers_to_letters[new_pos]
    return s

def decrypt(m):
    s = ""
    for char in m:
        current_pos = letters[char]
        new_pos = current_pos - 1
        if new_pos not in numbers_to_letters:
            new_pos = 26

        s += numbers_to_letters[new_pos]
    return s




print(encrypt("HALLO"))
print(decrypt(encrypt("HALLO")))






