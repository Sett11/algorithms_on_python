from re import sub
from math import ceil, inf
from collections import defaultdict, deque, Counter
from string import ascii_uppercase,digits
from gen_graph import matrix, dfs_a, dfs_b, seq, seq_b, generate_chess_knight_grafh, p_graph as g, d_graph as dg, k_graph as k
from pprint import pprint
from functools import lru_cache,reduce
from itertools import product
from operator import mul
from random import shuffle,choice#,randint


def pf(n):
    r,c=[],2
    while c<n*n:
        while n%c==0:
            n//=c
            r.append(c)
        c+=1
    return r

def get_all_divisors(n):
    return sorted(map(lambda x:reduce(mul,x,1),product(*[[j**i for i in range(k+1)] for j,k in Counter(pf(n)).items()])))

print(get_all_divisors(987000))