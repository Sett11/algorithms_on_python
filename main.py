from random import shuffle,choice#,randint
from re import sub
from math import ceil, inf
from collections import defaultdict, deque
from string import ascii_uppercase,digits
from gen_graph import matrix, dfs_a, dfs_b, seq, generate_chess_knight_grafh, p_graph as g, d_graph as dg
from pprint import pprint


def integer_partition(n):
    d=[1]+[0]*n
    for i in range(1,n+1):
        for j in range(i,n+1):
            d[j]+=d[j-i]
    return d[-1]

print(integer_partition(100))