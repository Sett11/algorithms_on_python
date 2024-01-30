from random import shuffle,choice#,randint
from re import sub
from math import ceil, inf
from collections import defaultdict, deque
from string import ascii_uppercase
from gen_graph import matrix, dfs_a, dfs_b, generate_chess_knight_grafh, p_graph as g, d_graph as dg

def f(a,j,r,q):
    if not r:
        t=[]
        for i in range(j):
            t.append(a[i])
        q.append(t)
        return
    p=1 if j==0 else a[j-1]
    for i in range(p,r+1):
        a[j]=i
        f(a,j+1,r-i,q)
    return q

def comb(n):
    return f([0]*n,0,n,[])

print(comb(22))