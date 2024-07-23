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


def g(a,r):
    p,n,res=tuple(a),len(a),[]
    t=[0]*r
    f=lambda:res.append(tuple(p[i] for i in t))
    f()
    while 1:
        for i in reversed(range(r)):
            if t[i]!=n-1:
                break
        else:
            return res
        t[i:]=[t[i]+1]*(r-i)
        f()

print(g([1,2,3,4],2))