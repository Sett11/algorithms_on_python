import gmpy2
import inspect
import networkx as nx
import matplotlib.pyplot as plt
import re
from math import ceil, inf
from collections import defaultdict, deque, Counter
from string import ascii_uppercase, digits
from gen_graph import matrix,dfs_a,dfs_b,seq,seq_b,generate_chess_knight_grafh,p_graph as g,d_graph as dg,f_grapf as fg, ff_g,exp,exp_dict,net_g,options,back
from functools import reduce
from itertools import product,zip_longest
from operator import mul,add,sub,truediv
from random import shuffle,choice#,randint
q=list(range(1,1503))
shuffle(q)

# BST

class Node:
    def __init__(self,val=None,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class BST:
    def __init__(self):
        self.root=Node()

    def add(self,v,h=None):
        h=h or self.root
        if h.val is None:
            h.val=v
        else:
            if v<=h.val:
                if not h.left:
                    h.left=Node(v)
                else:
                    self.add(v,h.left)
            else:
                if not h.right:
                    h.right=Node(v)
                else:
                    self.add(v,h.right)
    
    def get_min(self):
        v=None
        def f(x):
            nonlocal v
            if not x:
                return
            if not x.left:
                v=x.val
                return
            f(x.left)
        f(self.root)
        return v
    
    def get_max(self):
        v=None
        def f(x):
            nonlocal v
            if not x:
                return
            if not x.right:
                v=x.val
                return
            f(x.right)
        f(self.root)
        return v
    
    def __contains__(self,v):
        b=False
        def f(x):
            nonlocal b
            if not x or b:
                return
            if x.val==v:
                b=True
                return
            f(x.left)
            f(x.right)
        f(self.root)
        return b

    def __repr__(self):
        r=[]
        def f(x):
            if not x:
                return
            f(x.left)
            r.append(str(x.val))
            f(x.right)
        f(self.root)
        return ' - '.join(r)

t=BST()

[t.add(i) for i in q[:50]]
print(repr(t))
print(t.get_min(),t.get_max())