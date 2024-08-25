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

def encode_rail_fence_cipher(s,n):
    m=len(s)
    a=[[None for _ in range(m)] for __ in range(n)]
    i=j=d=0
    while j<m:
        a[i][j]=s[j]
        d=0 if i==n-1 else 1 if i==0 else d
        i=i+1 if d else i-1
        j+=1
    return ''.join(''.join(filter(bool,i)) for i in a)
    
def decode_rail_fence_cipher(s,n):
    m=len(s)
    a,r=[[None for _ in range(m)] for __ in range(n)],''
    i=j=d=g=0
    while j<m:
        a[i][j]='&'
        d=0 if i==n-1 else 1 if i==0 else d
        i=i+1 if d else i-1
        j+=1
    for i in range(n):
        for j in range(m):
            if a[i][j]=='&':
                a[i][j]=s[g]
                g+=1
    i=j=d=0
    while j<m:
        r+=a[i][j]
        d=0 if i==n-1 else 1 if i==0 else d
        i=i+1 if d else i-1
        j+=1
    return r

print(encode_rail_fence_cipher("Hello, World!", 4),sep='\n')
print(decode_rail_fence_cipher("H !e,Wdloollr", 4),sep='\n')