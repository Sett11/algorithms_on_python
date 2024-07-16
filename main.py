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


def ulam_sequence(a,b,n):
    sq,r=[0]*1000000,[a,b]
    sq[a+b]=1
    i=a+b
    while len(r)<n:
        if sq[i]==1:
            for j in r:
                sq[i+j]+=1
            r.append(i)
        i+=1
    return r

print(ulam_sequence(2,5,300))