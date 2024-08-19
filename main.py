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


class Vertex:
    def __init__(self,key):
        self.id=key
        self.connected_to={}
    
    def add_neigbords(self,k,w=0):
        self.connected_to[k]=w
    
    def connection(self):
        return self.connected_to.keys()
    
class Graph:
    def __init__(self):
        self.vertxs={}
        self.size=0

    def add_vert(self,k):
        self.size+=1
        v=Vertex(k)
        self.vertxs[k]=v
        return v
    
    def get_vert(self,k):
        if k in self.vertxs:
            return self.vertxs[k]
        
    def add_edge(self,k,v,w=0):
        if k not in self.vertxs:
            self.add_vert(k)
        if v not in self.vertxs:
            self.add_vert(v)
        self.vertxs[k].add_neigbords(self.vertxs[v],w)

    def get_vertexses(self):
        return self.vertxs.keys()
    
    def __contains__(self,k):
        return k in self.vertxs
    
    def __iter__(self):
        return iter(self.vertxs.values())
    
G=Graph()
[G.add_vert(i) for i in range(6)]
G.add_edge(0,1,5)
G.add_edge(0,5,2)
G.add_edge(1,2,4)
G.add_edge(2,3,9)
G.add_edge(3,4,7)
G.add_edge(3,5,3)
G.add_edge(4,0,1)
G.add_edge(5,4,8)
G.add_edge(5,2,1)

for i in G:
    for j in i.connection():
        print(i.id,j.id,i.connected_to[j])