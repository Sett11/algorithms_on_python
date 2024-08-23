import gmpy2
import inspect
import networkx as nx
import matplotlib.pyplot as plt
import re
from math import ceil,inf
from collections import defaultdict,deque,Counter
from string import ascii_uppercase,digits
from gen_graph import matrix,dfs_a,dfs_b,seq,seq_b,generate_chess_knight_grafh,p_graph as g,d_graph as dg,f_grapf as fg, ff_g,exp,exp_dict,net_g,options,back
from functools import reduce
from itertools import product,zip_longest
from copy import deepcopy
from operator import mul,add,sub,truediv
from random import shuffle,choice#,randint
q=list(range(1,1503))
shuffle(q)

def square_sums(n):
   sq,g={i*i:i for i in range(1,50)},{}
   for i in range(1,n+1):
      for j in range(1,n+1):
         if i!=j and i+j in sq:
            if i not in g:
               g[i]=[j]
            else:
               g[i].append(j)
   def ham(g,s,n,p):
      if s not in p:
         p.append(s)
         if len(p)==n:
            return p
         for i in g.get(s,[]):
            r=[i for i in p]
            t=ham(g,i,n,r)
            if t:
               return t
   for i in range(1,n+1):
      t=ham(g,i,n,[])
      if t:
         return t
   return False

print(square_sums(15))