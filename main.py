import numpy as np
import gmpy2
import inspect
import bisect
import networkx as nx
import matplotlib.pyplot as plt
import re
from math import ceil,floor,inf,factorial,log10,pi,e
from collections import defaultdict,deque,Counter
from string import ascii_uppercase,digits
from gen_graph import matrix,dfs_a,dfs_b,seq,seq_b,generate_chess_knight_grafh,p_graph as g,d_graph as dg,f_grapf as fg, ff_g,exp,exp_dict,net_g,options,back,sudoku,kad
from functools import reduce
from itertools import product,zip_longest,permutations
from copy import deepcopy
from operator import mul,add,sub,truediv,mod
from decimal import Decimal
from random import shuffle,choice#,randint
q=list(range(1,1503))
shuffle(q)
def fucken_indentations():
   ...

def count_subsequences(t,s):
    n,m=len(s),len(t)
    a=[0]*m
    for i in range(n):
        for j in range(m-1,-1,-1):
            if s[i]==t[j]:
                a[j]+=a[j-1] if j else 1
    return a[-1]

print(count_subsequences("happy birthday", "appyh appy birth day"))
print(count_subsequences("happy birthday", "hhaappyy bbiirrtthhddaayy"))