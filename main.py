from re import sub
from math import ceil, inf
from collections import defaultdict, deque, Counter
from string import ascii_uppercase, digits
from gen_graph import matrix, dfs_a, dfs_b, seq, seq_b, generate_chess_knight_grafh, p_graph as g, d_graph as dg, f_grapf as fg, ff_g
from functools import reduce
from itertools import product
from operator import mul
from random import shuffle,choice#,randint
q=list(range(1,1503))
shuffle(q)


def boyer_moore_horspool(s,t):
    n,m,u,d=len(s),len(t),set(),{}
    for i in range(m-2,-1,-1):
        if t[i] not in u:
            d[t[i]]=m-i-1
            u.add(t[i])
    if t[-1] not in u:
        d[t[-1]]=m
    if n>=m:
        i=m-1
        while i<n:
            j=k=0
            v=False
            for j in range(m-1,-1,-1):
                if s[i-k]!=t[j]:
                    if j==m-1:
                        off=d.get(s[i],m)
                    else:
                        off=d[t[j]]
                    i+=off
                    v=True
                    break
                k+=1
            if not v:
                return i-k+1
    return 'Not found...'



print(boyer_moore_horspool('nejvneoqhjvncjvbehjkbv jhkd,bv hjkvb hjkd,bv hrkdvb hk','hjkvb '))