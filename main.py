import gmpy2
import inspect
import networkx as nx
import matplotlib.pyplot as plt
import re
from math import ceil,inf,factorial
from collections import defaultdict,deque,Counter
from string import ascii_uppercase,digits
from gen_graph import matrix,dfs_a,dfs_b,seq,seq_b,generate_chess_knight_grafh,p_graph as g,d_graph as dg,f_grapf as fg, ff_g,exp,exp_dict,net_g,options,back,sudoku,kad
from functools import reduce
from itertools import product,zip_longest
from copy import deepcopy
from operator import mul,add,sub,truediv
from decimal import Decimal
from random import shuffle,choice#,randint
q=list(range(1,1503))
shuffle(q)

def kadane(a):
    m=n=0
    for i in a:
        n+=i
        if n>m:
            m=n
        if n<0:
            n=0
    return m

print(kadane(kad))