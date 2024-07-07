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


def factorial(n):
    return 1 if n<=1 else n*factorial(n-1)

def count_combinations(n,m):
    return factorial(n)//(factorial(m)*factorial(n-m))

print(count_combinations(10,5))