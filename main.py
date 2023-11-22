def gcd(a,b):
    return a if not b else gcd(b,a%b)

def lcm(a,b):
    n=gcd(a,b)
    return a*b/n if n else 0

print(lcm(18,15))