from math import ceil

def eratosthenus(n):
    if n<2:
        return []
    r=[True]*(n+1)
    r[0]=r[1]=False

    for i in range(2,int(n**.5+1)):
        if r[i]:
            r[2*i:n+1:i]=[False]*ceil(((n+1)/i)-2)

    return [i for i,j in enumerate(r) if j]


print(eratosthenus(10001))