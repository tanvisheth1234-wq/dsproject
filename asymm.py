#rsa

p = 3
q = 11

n = p * q
phi = (p - 1) * (q - 1)

e = 3
d = 7

print("Public key:", e, n)
print("Private key:", d, n)

msg = int(input("Enter message number: "))

# Encryption
c = pow(msg, e, n)
print("Encrypted message:", c)

# Decryption
m = pow(c, d, n)
print("Decrypted message:", m)

#ElGamal 

p = 23
g = 5

x = 6
y = pow(g, x, p)

print("Public key:", p, g, y)
print("Private key:", x)

msg = int(input("Enter message number: "))
k = 3

# Encryption
c1 = pow(g, k, p)
c2 = (msg * pow(y, k, p)) % p

print("Encrypted message:", c1, c2)

# Decryption
s = pow(c1, x, p)
s_inv = pow(s, -1, p)

m = (c2 * s_inv) % p

print("Decrypted message:", m)

#Diffie hellman

p = 23
g = 5

# Alice's private key
a = 6

# Bob's private key
b = 15

# Public keys
A = pow(g, a, p)
B = pow(g, b, p)

print("Alice's public key:", A)
print("Bob's public key:", B)

# Shared secret keys
key1 = pow(B, a, p)
key2 = pow(A, b, p)

print("Alice's shared key:", key1)
print("Bob's shared key:", key2)

if key1 == key2:
    print("Shared key established successfully")

#ecc

p = 17
a = 2
b = 2

G = (5, 1)   # Generator point

def add(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and (y1 + y2) % p == 0:
        return None

    if P == Q:
        m = (3*x1*x1 + a) * pow(2*y1, -1, p) % p
    else:
        m = (y2-y1) * pow(x2-x1, -1, p) % p

    x3 = (m*m-x1-x2) % p
    y3 = (m*(x1-x3)-y1) % p

    return (x3, y3)

def multiply(k, P):
    R = None
    for i in range(k):
        R = add(R, P)
    return R

private = 5
public = multiply(private, G)

print("Private key:", private)
print("Public key:", public)

