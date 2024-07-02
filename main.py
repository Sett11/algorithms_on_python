from re import sub
from math import ceil, inf
from collections import defaultdict, deque, Counter
from string import ascii_uppercase,digits
from gen_graph import matrix, dfs_a, dfs_b, seq, seq_b, generate_chess_knight_grafh, p_graph as g, d_graph as dg, f_grapf as fg, ff_g
from pprint import pprint
from functools import lru_cache,reduce
from itertools import product
from operator import mul
from random import shuffle,choice#,randint


class Node:
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
    def __repr__(self):
        return f'Node({self.data}, {self.left}, {self.right})'
    
a,b,c,d,e=Node(1),Node(2),Node(3),Node(4),Node(5)
a.left=b
a.right=c
b.left=d
c.right=e

def pre_order(h):
    r=[]
    def f(x):
        if not x:
            return
        r.append(x.data)
        f(x.left)
        f(x.right)
    f(h)
    return r

def in_order(h):
    r=[]
    def f(x):
        if not x:
            return
        f(x.left)
        r.append(x.data)
        f(x.right)
    f(h)
    return r

def post_order(h):
    r=[]
    def f(x):
        if not x:
            return
        f(x.left)
        f(x.right)
        r.append(x.data)
    f(h)
    return r

print(pre_order(a))
print(in_order(a))
print(post_order(a))