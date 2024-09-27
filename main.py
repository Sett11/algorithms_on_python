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



import heapq as h


class Node:
    def __init__(self,s=None,n=None,l=None,r=None):
        self.s=s
        self.n=n
        self.l=l
        self.r=r
    
    def __lt__(self,other):
        return self.n<other.n

def build_haffman_tree(a):
    q=[Node(*i) for i in a]
    h.heapify(q)
    while len(q)>1:
        l,r=h.heappop(q),h.heappop(q)
        m=Node(n=l.n+r.n)
        m.l,m.r=l,r
        h.heappush(q,m)
    return q[0]

def gen_haffman_code(n,c='',r={}):
    if n is not None:
        if n.s is not None:
            r[n.s]=c
        gen_haffman_code(n.l,c+'0',r)
        gen_haffman_code(n.r,c+'1',r)
    return r

def search_letters(a,s,x,q,n,z):
    if x==z:
        return q
    for i in range(n,0,-1):
        t=s[:i]
        if t in a:
            w=search_letters(a,s[i:],x+t,q+[a[t]],n,z)
            if w:
                return w

def frequencies(s):
    return list(Counter(s).items())

def encode(f,s):
    if len(f)<2:
        return
    if not s:
        return ''
    r=gen_haffman_code(build_haffman_tree(f))
    return ''.join(r[i] for i in s)
  
def decode(f,b):
    if len(f)<2:
        return
    if not b:
        return ''
    r=dict([i[::-1] for i in gen_haffman_code(build_haffman_tree(f)).items()])
    return ''.join(search_letters(r,b,'',[],len(max(r,key=len)),b))

print(encode(frequencies('mdj'),'mdj'))
print(decode(frequencies('mdj'),'01110'))