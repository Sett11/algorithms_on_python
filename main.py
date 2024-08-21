import gmpy2
import inspect
import networkx as nx
import matplotlib.pyplot as plt
import re
from math import ceil, inf
from collections import defaultdict, deque, Counter
from string import ascii_uppercase, digits
from gen_graph import matrix,dfs_a,dfs_b,seq,seq_b,generate_chess_knight_grafh,p_graph as g,d_graph as dg,f_grapf as fg, ff_g,exp,exp_dict,net_g,options,back
from functools import reduce
from itertools import product,zip_longest
from operator import mul,add,sub,truediv
from random import shuffle,choice#,randint
q=list(range(1,1503))
shuffle(q)

def subsets(a):
    r=[[]]
    for i in a:
        r+=[x+[i] for x in r]
    return r

print(subsets([1,2,3,4]))