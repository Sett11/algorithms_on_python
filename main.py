from random import shuffle

def min_elem(a):
    n=float('inf')
    for i in range(len(a)):
        n=n if n<a[i] else a[i]
    return n

def ind_min_elem(a,n):
    return next(i for i in range(len(a)) if a[i]==n)

def del_min_elem(a,n):
    for i in range(len(a)):
        if a[i]==n:
            del a[i]
            return a


def dumb_sort(a):
    r=[]
    while len(a)>1:
        j=ind_min_elem(a,min_elem(a))
        r.append(a[j])
        a=del_min_elem(a,a[j])
    return r+a


q = list(range(101))
shuffle(q)
print(dumb_sort(q))
