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

def radix_tree(*a):
    d={}
    for i in a:
        if i:
            d[i[0]]=d.get(i[0],[])+[i[1:]]
    z={}
    for i in d:
        t=radix_tree(*d[i])
        if len(t)==1 and '' not in d[i]:
            for j in t:
                i,t=i+j,t[j]
        z[i]=t
    return z

print(radix_tree("apple", "applet", "apple", "ape"))