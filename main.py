from random import randint

def miller_rabin_test(n,k=5):
    if n<2:
        return False
    if n<4:
        return True
    
    r,s=0,n-1

    while s%2==0:
        r+=1
        s//=2

    for _ in range(k):
        a=randint(2,n-1)
        x=pow(a,s,n)
        if x==1 or x==n-1:
            continue
        for __ in range(r-1):
            x=pow(x,2,n)
            if x==n-1:
                break
        else:
            return False
    return True

print(miller_rabin_test(997))