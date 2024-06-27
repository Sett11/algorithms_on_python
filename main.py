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


def bit_sum(a,b):
    return a if not b else bit_sum(a^b,(a&b)<<1)

print(bit_sum(5,7))