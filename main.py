from random import shuffle,choice#,randint
from re import sub
from math import ceil, inf
from collections import defaultdict, deque
from string import ascii_uppercase,digits
from gen_graph import matrix, dfs_a, dfs_b, seq, generate_chess_knight_grafh, p_graph as g, d_graph as dg
from pprint import pprint

def points(n):
    return 1+4*sum((n*n-i*i)**.5//1 for i in range(n))


print(points(1000))