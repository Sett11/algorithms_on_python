def left(a,n):
    l=1
    r=len(a)
    while r-l>1:
        m=(l+r)//2
        if a[m]<n:
            l=m
        else:
            r=m
    return l+1

def right(a,n):
    l=1
    r=len(a)
    while r-l>1:
        m=(l+r)//2
        if a[m]<=n:
            l=m
        else:
            r=m
    return r

def binary_search(a,n):
    return n in a[left(a,n):right(a,n)]

print(binary_search([0, 1, 1, 2, 3, 3, 4, 4, 6, 59],3))