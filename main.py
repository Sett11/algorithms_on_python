import gmpy2
import inspect
import re
from math import ceil, inf
from collections import defaultdict, deque, Counter
from string import ascii_uppercase, digits
from gen_graph import matrix,dfs_a,dfs_b,seq,seq_b,generate_chess_knight_grafh,p_graph as g,d_graph as dg,f_grapf as fg, ff_g,exp,exp_dict,LazyInit
from functools import reduce
from itertools import product
from operator import mul,add,sub,truediv
from random import shuffle,choice#,randint
q=list(range(1,1503))
shuffle(q)

def f(*a):
    tree={}
    for i in a:
        l,node=len(i),tree
        for j in range(1,l+1):
            x=i[:j]
            node[x]=node={} if l-j and node.get(x) is None else node.get(x)
    return tree

print(f('true','trie'))