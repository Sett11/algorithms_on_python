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



from re import split,findall
from functools import reduce

def f(e,x):
    k,p=split(r'x\^?',e)
    k,p=-1 if k=='-' else 1 if k=='' else int(k),1 if p=='' else int(p)
    return p*k*pow(x,p-1)

def differentiate(e,p):
    return reduce(lambda a,c:a+f(c,p),[i[0] for i in findall(r'(-?\d*x(\^\d+)?)',e)],0)