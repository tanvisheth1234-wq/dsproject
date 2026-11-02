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

text = input("Enter 2-letter plaintext: ").upper()

a = ord(text[0]) - 65
b = ord(text[1]) - 65

# Key matrix
k1, k2 = 3, 3
k3, k4 = 2, 5

# Encryption
c1 = (k1*a + k2*b) % 26
c2 = (k3*a + k4*b) % 26

encrypted = chr(c1 + 65) + chr(c2 + 65)
print("Encrypted text:", encrypted)

# Decryption
det = (k1*k4 - k2*k3) % 26
inv = 9  # Modular inverse of 9 is 3

d1 = (inv * (k4*c1 - k2*c2)) % 26
d2 = (inv * (-k3*c1 + k1*c2)) % 26

decrypted = chr(d1 + 65) + chr(d2 + 65)
print("Decrypted text:", decrypted)

