#Caesar Cipher

text = input("Enter plaintext: ")
key = int(input("Enter key: "))

encrypted = ""

# Encryption
for ch in text:
    if ch.isupper():
        encrypted += chr((ord(ch) - 65 + key) % 26 + 65)
    elif ch.islower():
        encrypted += chr((ord(ch) - 97 + key) % 26 + 97)
    else:
        encrypted += ch

print("Encrypted text:", encrypted)

# Decryption
decrypted = ""

for ch in encrypted:
    if ch.isupper():
        decrypted += chr((ord(ch) - 65 - key) % 26 + 65)
    elif ch.islower():
        decrypted += chr((ord(ch) - 97 - key) % 26 + 97)
    else:
        decrypted += ch

print("Decrypted text:", decrypted)

#Monoalphabetic

text = input("Enter plaintext: ").upper()

key = "QWERTYUIOPASDFGHJKLZXCVBNM"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

encrypted = ""

for ch in text:
    if ch in alphabet:
        encrypted += key[alphabet.index(ch)]
    else:
        encrypted += ch

print("Encrypted text:", encrypted)

decrypted = ""

for ch in encrypted:
    if ch in key:
        decrypted += alphabet[key.index(ch)]
    else:
        decrypted += ch

print("Decrypted text:", decrypted)

#Vigenère

text = input("Enter plaintext: ").upper()
key = input("Enter key: ").upper()

encrypted = ""
decrypted = ""

for i in range(len(text)):
    if text[i].isalpha():
        p = ord(text[i]) - 65
        k = ord(key[i % len(key)]) - 65

        c = (p + k) % 26
        encrypted += chr(c + 65)

print("Encrypted text:", encrypted)

for i in range(len(encrypted)):
    p = ord(encrypted[i]) - 65
    k = ord(key[i % len(key)]) - 65

    c = (p - k) % 26
    decrypted += chr(c + 65)

print("Decrypted text:", decrypted)

#Playfair 

key = "MONARCHY"
text = input("Enter plaintext: ").upper().replace("J", "I")

alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
matrix = ""

for ch in key + alphabet:
    if ch in alphabet and ch not in matrix:
        matrix += ch

print("Key Matrix:")

for i in range(0, 25, 5):
    print(matrix[i:i+5])

text = text.replace(" ", "")
pairs = ""

i = 0
while i < len(text):
    a = text[i]

    if i + 1 == len(text):
        b = "X"
        i += 1
    elif text[i] == text[i+1]:
        b = "X"
        i += 1
    else:
        b = text[i+1]
        i += 2

    pairs += a + b

encrypted = ""

for i in range(0, len(pairs), 2):
    a = pairs[i]
    b = pairs[i+1]

    x = matrix.index(a)
    y = matrix.index(b)

    r1, c1 = x // 5, x % 5
    r2, c2 = y // 5, y % 5

    if r1 == r2:
        encrypted += matrix[r1*5 + (c1+1)%5]
        encrypted += matrix[r2*5 + (c2+1)%5]
    elif c1 == c2:
        encrypted += matrix[((r1+1)%5)*5 + c1]
        encrypted += matrix[((r2+1)%5)*5 + c2]
    else:
        encrypted += matrix[r1*5 + c2]
        encrypted += matrix[r2*5 + c1]

print("Encrypted text:", encrypted)

#Hill Cipher


def mod_inverse(a):
    for i in range(26):
        if (a * i) % 26 == 1:
            return i
    return -1


def encrypt(text, key):
    text = text.upper().replace(" ", "")

    if len(text) % 2 != 0:
        text += "X"

    result = ""

    for i in range(0, len(text), 2):
        x = ord(text[i]) - 65
        y = ord(text[i+1]) - 65

        c1 = (key[0][0]*x + key[0][1]*y) % 26
        c2 = (key[1][0]*x + key[1][1]*y) % 26

        result += chr(c1+65) + chr(c2+65)

    return result


def decrypt(text, key):
    a, b = key[0]
    c, d = key[1]

    det = (a*d - b*c) % 26
    inv = mod_inverse(det)

    if inv == -1:
        return "Invalid key"

    inverse_key = [
        [d*inv % 26, -b*inv % 26],
        [-c*inv % 26, a*inv % 26]
    ]

    return encrypt(text, inverse_key)


key = [[3, 3], [2, 5]]

text = input("Enter plaintext: ")

cipher = encrypt(text, key)

print("Encrypted text:", cipher)
print("Decrypted text:", decrypt(cipher, key))


