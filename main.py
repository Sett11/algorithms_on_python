def gcd(a,b):
    return a if not b else gcd(b,a%b)


print(gcd(70,49))
print(gcd(49,70))