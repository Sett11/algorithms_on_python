import gmpy2
import inspect
import networkx as nx
import matplotlib.pyplot as plt
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

def f(x,y,a):
    g=nx.DiGraph()
    for i in a:
        if i not in g:
            g.add_node(i)
            for j in a[i]:
                if j not in g:
                    g.add_node(j)
                g.add_edge(i,j,weight=a[i][j])
    #path=nx.shortest_path(g,x,y,lambda x,y,_:g[x][y]['weight'])
    options={
    'node_color':'pink',
    'node_size':2000,
    'width':1,
    'arrowstyle':'-|>',
    'arrowsize':29,
    'edge_color':'yellow',
}
    pos=nx.circular_layout(g)
    nx.draw(g,pos,with_labels=True,font_weight='bold',**options)
    nx.draw_networkx_edge_labels(g,pos,edge_labels={(j[0],j[1]):g[j[0]][j[1]]['weight'] for j in g.edges})
    plt.show()

print(f('A','E',dg))