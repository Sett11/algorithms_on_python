from random import shuffle,choice#,randint
from re import sub
from math import ceil, inf
from collections import defaultdict, deque
from string import ascii_uppercase,digits
from gen_graph import matrix, dfs_a, dfs_b, seq, seq_p, generate_chess_knight_grafh, p_graph as g, d_graph as dg
from pprint import pprint


def prime_fac(n):
    r,i=[],2
    while i<n**2:
        while n%i==0:
            r.append(i)
            n//=i
        i+=1
    return r

print(prime_fac(94080000))