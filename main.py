from random import shuffle,choice#,randint
from re import sub
from math import ceil,inf
from collections import defaultdict,deque
from string import ascii_uppercase
from gen_graph import matrix


def f(a,j,n,r,q=[]):
    if(r<0):
        return
    if(r==0):
        t=[]
        for i in range(j):
            t.append(a[i])
        q.append(t)
        return
    p=1 if j==0 else a[j-1]
    for k in range(p,n+1):
        a[j]=k
        f(a,j+1,n,r-k,q)
    return q

def combos(n):
    return f([0]*n,0,n,n,[])

print(combos(13))