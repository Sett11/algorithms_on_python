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
from itertools import product,zip_longest,permutations
from copy import deepcopy
from operator import mul,add,sub,truediv,mod
from decimal import Decimal
from random import shuffle,choice#,randint
q=list(range(1,1503))
shuffle(q)
def fucken_indentations():
   ...

def bouncy_count(n):
   a,b,t=[1]*9,[1]*9,10
   for _ in range(2,n+1):
      c,d=[0]*9,[1]*9
      x=y=0
      for j in range(8,-1,-1):
         x+=a[j]
         c[j]+=x
         t+=c[j]
      for j in range(9):
         y+=b[j]
         d[j]+=y
         t+=d[j]
      t-=9
      a,b,c,d=c,d,a,b
   return 10**n-t if n else 0

print(bouncy_count(4))