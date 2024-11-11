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



def encoder(s):
    d,r,c,k={s[0]:'1'},'0'+s[0],2,''
    for i in s[1:]:
        k+=i
        if k not in d:
            d[k]=str(c)
            if len(k)==1:
                r+='0'+k
            else:
                r+=d[k[0:-1]]+k[-1]
            c+=1
            k=''
    return r+d.get(k,'')

def decoder(s):
    d,r,c,k={'0':'','1':s[1]},s[1],'',2
    for i in s[2:]:
        if i.isdigit():
            c+=i
        else:
            d[str(k)]=d[c]+i
            r+=d[c]+i
            c=''
            k+=1
    return r+d.get(c,'')

print(encoder('ABAABABAABABAA'))
print(decoder('0A0B1A2A4A4B3'))