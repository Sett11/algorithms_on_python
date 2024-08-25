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
def fucken_indentations():
   ...

def kadane(a): 
    m,c=float('-inf'),0
    for i in a:
        c+=i
        m=c if m<c else m
        c=0 if c<0 else c
    return m

def maxSubmatrixSum(a): 
    n,m,M=len(a),len(a[0]),float('-inf')
    r=[[0 for _ in range(m)] for __ in range(n)]
    for i in range(n):
        for j in range(m):
            r[i][j]=a[i][j] if not j else a[i][j]+r[i][j-1]
    for i in range(m):
        for j in range(i,m):
            t=[]
            for k in range(n):
                t.append(r[k][j] if not i else r[k][j]-r[k][i-1])
            M=max(M,kadane(t))
    return M

print(maxSubmatrixSum(matrix))