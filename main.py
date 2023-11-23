from random import shuffle

def merge(a,b):
    n,m=len(a),len(b)
    r=[0]*(n+m)
    i=j=k=0

    while i<n and j<m:
        if a[i]<=b[j]:
            r[k]=a[i]
            i+=1
        else:
            r[k]=b[j]
            j+=1
        k+=1
    
    while i<n:
        r[k]=a[i]
        i+=1
        k+=1

    while j<m:
        r[k]=b[j]
        j+=1
        k+=1

    return r


def merge_sort(a):
    n=len(a)
    if n<2:
        return
    m=n//2
    l=[a[i] for i in range(m)]
    r=[a[i] for i in range(m,n)]
    merge_sort(l)
    merge_sort(r)
    c=merge(l,r)

    for i in range(len(c)):
        a[i]=c[i]

    return a

q=list(range(1002))
shuffle(q)


print(merge_sort(q))