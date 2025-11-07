letters = {chr(65 + i): i + 1 for i in range(26)}  # ASACII
numbers_to_letters = {v: k for k, v in letters.items()}

def shift_string(m, step):
    result = ""
    for char in m:
        if char not in letters:
            result += char  # falls z.B. Leerzeichen
            continue
        new_pos = (letters[char] - 1 + step) % 26 + 1  # mit -1 wird auf 0-25 verschoben
        result += numbers_to_letters[new_pos]
    return result

def encrypt(m):
    return shift_string(m, 1)

def decrypt(m):
    return shift_string(m, -1)