import gmpy2
import inspect
import networkx as nx
import matplotlib.pyplot as plt
import re
from math import ceil,inf,factorial
from collections import defaultdict,deque,Counter
from string import ascii_uppercase,digits
from gen_graph import matrix,dfs_a,dfs_b,seq,seq_b,generate_chess_knight_grafh,p_graph as g,d_graph as dg,f_grapf as fg, ff_g,exp,exp_dict,net_g,options,back,sudoku
from functools import reduce
from itertools import product,zip_longest
from copy import deepcopy
from operator import mul,add,sub,truediv
from decimal import Decimal
from random import shuffle,choice#,randint
q=list(range(1,1503))
shuffle(q)

def list_position(w):
   s,c=sorted(w),1
   for i in w:
        if i==s[0]:
            s.pop(0)
            continue
        p=s.index(i)
        c+=(p*Decimal(factorial(len(s)-1)/reduce(mul,map(factorial,Counter(s).values()))))
        s.pop(p)
   return c

print(list_position('QUESTION'))