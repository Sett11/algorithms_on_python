import gmpy2
import inspect
import re
from math import ceil, inf
from collections import defaultdict, deque, Counter
from string import ascii_uppercase, digits
from gen_graph import matrix,dfs_a,dfs_b,seq,seq_b,generate_chess_knight_grafh,p_graph as g,d_graph as dg,f_grapf as fg, ff_g,exp,exp_dict,net_g
from functools import reduce
from itertools import product,zip_longest
from operator import mul,add,sub,truediv
from random import shuffle,choice#,randint
q=list(range(1,1503))
shuffle(q)

import networkx as nx

def shortest(start,end,a):
    G=nx.DiGraph()
    for i,j,k in a:
        G.add_node(i)
        G.add_edge(i,j,weight=k)
    p=nx.shortest_path(G,start,end,lambda x,y,z:G[x][y]['weight'],method='bellman-ford')
    return p,sum([G[p[i]][p[i+1]]['weight'] for i in range(len(p)-1)])

print(shortest('A','C',net_g))