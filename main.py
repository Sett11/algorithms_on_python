from random import shuffle,choice#,randint
from re import sub
from math import ceil, inf
from collections import defaultdict, deque
from string import ascii_uppercase
from gen_graph import matrix, dfs_a, dfs_b, generate_chess_knight_grafh, p_graph as g, d_graph as dg


def depth_list(a):
    return 1+max(depth_list(i) for i in a) if a and isinstance(a,list) else 0

print(depth_list([[[[]]]]))