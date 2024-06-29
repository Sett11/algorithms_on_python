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


def gen_gray_code(n):
    a,r,j=[0]*(n+1),[],0
    while True:
        r.append(''.join(map(str,a[n-1::-1])))
        a[n]=1-a[n]
        if a[n]==1:
            j=0
        else:
            for i in range(n):
                if a[i]==1:
                    j=i+1
                    break
        if j>=n:
            break
        a[j]=1-a[j]
    return r


print(*gen_gray_code(3),sep='\n')