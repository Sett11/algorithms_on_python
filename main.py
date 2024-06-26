from re import sub
from math import ceil, inf
from collections import defaultdict, deque, Counter
from string import ascii_uppercase,digits
from gen_graph import matrix, dfs_a, dfs_b, seq, seq_b, generate_chess_knight_grafh, p_graph as g, d_graph as dg, f_grapf as fg
from pprint import pprint
from functools import lru_cache,reduce
from itertools import product
from operator import mul
from random import shuffle,choice#,randint


def get_path(a,i,j):
    r=[i]
    while i!=j:
        i=a[i][j]
        r.append(i)
    return r

def floyd(a,x,y):
    n=len(a)
    r=[[i for i in range(n)] for _ in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                v=a[i][k]+a[k][j]
                if a[i][j]>v:
                    a[i][j]=v
                    r[i][j]=k
    return get_path(r,y,x)


print(floyd(fg,4,1))