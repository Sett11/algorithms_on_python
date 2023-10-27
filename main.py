def largest_increacing_subcequence(a):
    n=len(a)
    r=[0]*(n+1)
    for i in range(1,n+1):
        m=0
        for j in range(i):
            if a[i-1]>a[j-1] and r[j]>m:
                m=r[j]
        r[i]=m+1
    return r[-1]

print(largest_increacing_subcequence([1,2,3,4,4,4,4,5,6,7]))