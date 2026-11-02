#dsads--------
def inverse(a, m):
    for i in range(1, m):
        if a * i % m == 1:
            return i


def hash_message(message, mod):
    h = 0

    for ch in message:
        h = (h * 31 + ord(ch)) % mod

    return h


p, q, g = 23, 11, 2

x = 6
y = pow(g, x, p)

message = input("Enter message: ")
h = hash_message(message, q)

k = 3

r = pow(g, k, p) % q
s = inverse(k, q) * (h + x * r) % q

print("Signature:", r, s)

w = inverse(s, q)

u1 = h * w % q
u2 = r * w % q

v = (pow(g, u1, p) * pow(y, u2, p) % p) % q

if v == r:
    print("Signature valid")
else:
    print("Signature invalid")




#ecdsads-----------

def inverse(a, p):
    for i in range(1, p):
        if a * i % p == 1:
            return i


def add(P, Q, a, p):
    if P is None:
        return Q

    if Q is None:
        return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and (y1 + y2) % p == 0:
        return None

    if P == Q:
        slope = (3*x1*x1 + a) * inverse(2*y1 % p, p) % p
    else:
        slope = (y2-y1) * inverse((x2-x1) % p, p) % p

    x3 = (slope*slope - x1 - x2) % p
    y3 = (slope*(x1-x3) - y1) % p

    return (x3, y3)


def multiply(k, P, a, p):
    R = None

    while k:
        if k % 2:
            R = add(R, P, a, p)

        P = add(P, P, a, p)
        k //= 2

    return R


def hash_message(message, mod):
    h = 0

    for ch in message:
        h = (h * 31 + ord(ch)) % mod

    return h


p, a, n = 17, 2, 19
G = (5, 1)

d = 7
Q = multiply(d, G, a, p)

message = input("Enter message: ")
h = hash_message(message, n)

k = 3

R = multiply(k, G, a, p)

r = R[0] % n
s = inverse(k, n) * (h + d*r) % n

print("Signature:", r, s)

w = inverse(s, n)

u1 = h * w % n
u2 = r * w % n

P1 = multiply(u1, G, a, p)
P2 = multiply(u2, Q, a, p)

V = add(P1, P2, a, p)

if V is not None and V[0] % n == r:
    print("Signature valid")
else:
    print("Signature invalid")


#egds--------
def inverse(a, m):
    for i in range(1, m):
        if a * i % m == 1:
            return i


def hash_message(message, mod):
    h = 0

    for ch in message:
        h = (h * 31 + ord(ch)) % mod

    return h


p, g = 23, 5

x = 6
y = pow(g, x, p)

message = input("Enter message: ")
h = hash_message(message, p - 1)

k = 7

r = pow(g, k, p)
s = inverse(k, p - 1) * (h - x * r) % (p - 1)

print("Signature:", r, s)

if pow(g, h, p) == (pow(y, r, p) * pow(r, s, p)) % p:
    print("Signature valid")
else:
    print("Signature invalid")


#rsads---------
def inverse(a, m):
    for i in range(1, m):
        if a * i % m == 1:
            return i


def hash_message(message, mod):
    h = 0

    for ch in message:
        h = (h * 31 + ord(ch)) % mod

    return h


p, q = 11, 13

n = p * q
phi = (p - 1) * (q - 1)

e = 7
d = inverse(e, phi)

message = input("Enter message: ")
h = hash_message(message, n)

signature = pow(h, d, n)

print("Signature:", signature)

if pow(signature, e, n) == h:
    print("Signature valid")
else:
    print("Signature invalid")


#schds------
def hash_message(message, mod):
    h = 0

    for ch in message:
        h = (h * 31 + ord(ch)) % mod

    return h


p, q, g = 23, 11, 2

x = 6
y = pow(g, x, p)

message = input("Enter message: ")
k = 3

r = pow(g, k, p)
e = hash_message(message + str(r), q)

s = (k + x * e) % q

print("Signature:", e, s)

if pow(g, s, p) == (r * pow(y, e, p)) % p:
    print("Signature valid")
else:
    print("Signature invalid")