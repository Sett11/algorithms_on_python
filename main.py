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

class Graph:
    def __init__(self):
        self.nodes={}

    def add_node(self,v):
        self.nodes[v]={}
    
    def add_edge(self,v,n,w=0):
        if v not in self.nodes:
            self.nodes[v]={}
        if n not in self.nodes:
            self.nodes[n]={}
        self.nodes[v][n]=w
        self.nodes[n][v]=w
    
    def __repr__(self):
        r=[]
        for i in self.nodes:
            s=f'{i} -> '
            for j in self.nodes[i]:
                s+=f'{j} '
            r.append(s)
        return '\n'.join(r)
    
g=Graph()

g.add_edge(1,2,9)
g.add_edge(1,7,11)
g.add_edge(1,4,10)
g.add_edge(2,6,11)
print(repr(g))