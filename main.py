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

def prefix_tree(*args):
    t={}
    def insert(s):
        c,x,n=t,'',len(s)
        for i in range(n):
            x+=s[i]
            if x in c and c[x] is None and i!=n-1:
                c[x]={}
            if x not in c:
                c[x]={} if i!=n-1 else None
            c=c[x]
    for i in args:
       insert(i)
    return t
   
print(prefix_tree("A","to", "tea", "ted", "ten", "i","in","inn"))