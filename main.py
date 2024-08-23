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

def f(n):
    return 1 if n==1 else n*f(n-1)

def count_combinations_with_repeated_simbols(a):
    return f(len(a))//reduce(mul,map(f,Counter(a).values()))

print(count_combinations_with_repeated_simbols(['0', '5', '3', '0', '4', '3', '2']))