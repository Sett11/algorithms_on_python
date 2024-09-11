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
q=list(range(1,1503))
shuffle(q)
def fucken_indentations():
   ...


# def regression_line_with_np(x,y):
#     a,b=np.polyfit(x,y,1)
#     return round(b,4),round(a,4)

def regression_line(x,y):
    n,xq,xs,ys,xys=len(x),sum(i**2 for i in x),sum(x),sum(y),sum(i*j for i,j in zip(x,y))
    k=n*xq-xs**2
    return round((xq*ys-xs*xys)/k,4),round((n*xys-xs*ys)/k,4)

print(regression_line([56,42,72,36,63,47,55,49,38,42,68,60],[147,125,160,118,149,128,150,145,115,140,152,155]))