def primes(n):
    if n<3:
        return 0
    a=[True]*(n+1)
    a[0]=a[1]=False
    for i in range(2,int(n**.5)+1):
        if a[i]:
            for j in range(i*i,n,i):
                a[j]=False
    return [k for k in range(2,n) if a[k]]

print(primes(100000))