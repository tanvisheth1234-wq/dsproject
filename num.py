#fermat
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(input("Enter a number: "))
a = int(input("Enter base: "))

if n <= 1:
    print("Composite")
elif n == 2:
    print("Prime")
elif gcd(a, n) != 1:
    print("Composite")
else:
    result = pow(a, n - 1, n)

    if result == 1:
        print("Probably Prime")
    else:
        print("Composite")

#rabin miller

n = int(input("Enter a number: "))

if n < 2:
    print("Composite")

elif n == 2 or n == 3:
    print("Prime")

elif n % 2 == 0:
    print("Composite")

else:
    a = int(input("Enter base: "))

    # Step 1: Find n-1 = 2^s * d
    d = n - 1
    s = 0

    while d % 2 == 0:
        d = d // 2
        s = s + 1

    # Step 2: Calculate a^d mod n
    x = pow(a, d, n)

    if x == 1 or x == n - 1:
        print("Probably Prime")

    else:
        for i in range(s - 1):
            x = (x * x) % n

            if x == n - 1:
                break

        if x == n - 1:
            print("Probably Prime")
        else:
            print("Composite")

#euler

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(input("Enter a number: "))
a = int(input("Enter base: "))

if n <= 1:
    print("Composite")
elif n == 2:
    print("Prime")
elif n % 2 == 0:
    print("Composite")
elif gcd(a, n) != 1:
    print("Composite")
else:
    result = pow(a, (n - 1) // 2, n)

    if result == 1 or result == n - 1:
        print("Probably Prime")
    else:
        print("Composite")


# Chinese Remainder Theorem

a = [2, 3, 2]       # Remainders
m = [3, 5, 7]       # Moduli

M = 1
for i in range(len(m)):
    M *= m[i]

result = 0

for i in range(len(m)):
    Mi = M // m[i]

    # Find modular inverse
    for j in range(m[i]):
        if (Mi * j) % m[i] == 1:
            inverse = j
            break

    result += a[i] * Mi * inverse

x = result % M

print("The solution is:", x)