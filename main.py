def primes(n):
    if n<2:
        return 0
    a=[True]*(n+1)
    a[0]=a[1]=False
    for i in range(2,int(n**.5)+1):
        for j in range(i*i,n,i):
            a[j]=False
    return [k for k in range(2,n) if a[k]]

print(primes(1000))