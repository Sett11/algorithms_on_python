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


def knuth_morris_pratt(s,t):
    n,m=len(s),len(t)
    p=[0]*m
    i,j=1,0
    while i<m:
        if t[i]==t[j]:
            p[i]=j+1
            i+=1
            j+=1
        else:
            if j==0:
                p[i]=0
                i+=1
            else:
                j=p[j-1]
    i=j=0
    while i<n:
        if s[i]==t[j]:
            i+=1
            j+=1
            if j==m:
                return i-m
        else:
            if j>0:
                j=p[j-1]
            else:
                i+=1
    return 'Not found...'

print(knuth_morris_pratt('aunntlammauaujjdau','lamm'))