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



import sympy as sym
from sympy.parsing.sympy_parser import standard_transformations as t
from sympy.parsing.sympy_parser import parse_expr as p
from re import findall, sub

def f(s):
    return sub(r'\d+[A-Za-z]+', lambda x: ''.join(i for i in x.group() if i.isdigit())+'*'+''.join(i for i in x.group() if i.isalpha()), s)

def solve(*a):
    r,u=[],set()
    for i in a:
        u.update(findall(r'[A-Za-z]+',i))
        r.append(tuple(f(i).split('=')))
    return sym.solve([sym.Eq(p(x,transformations=t), p(y,transformations=t)) for x,y in r],tuple(sym.symbols(sorted(u))))

print(solve('-40r-3257+61v-83x-22u-8u+25t+94p+35s-25q+6y+14z-5w-101t=-17t+38y-51z+1036', '-89p-30x-106s+7v-79u+18r+26w-56w-21y+59x-46q+56y+33z-69t+10t=-12s+40t-20305', '-68z+97w-78v-54x+19p+2735+66s-22r+23u+89r+20p-62t-52q-11y=-2795-2827-25y+26s-2805', '-13r+5r+29t-24t-113x-91v+6z-38u-44p-19p+29t+3z+18x-26q+11w-85s+41y=-2p+8q-8y-6926+49u+12y-26w', '-52x+52v+99s-92z-26q-58u-71q-40p-3u-26w-83r-43t+71y+28p-30s=-21t-4728-47p-2s', '78q-79x+82w-52p+41t+68t-76r-20v-20r+11y-4273-26z+19u-48v-21s=12682+25t+7x+11q+38u', '-34r-22p+26y+5w-3q+76u-34p-24z+20w+40t+34r-87x-60s-96v=43z+36y+10471+18q', '-48u+34s+4800-31q-13t+16q+60r+35x+20x+41z-22y+76p-43y-6z+49s+36w-97v-24q=41t-10q+20t-14335', '-100x-70y-19z+121q+33w+84p-59s+97u+34v-25r-19v-33t=17z-51r+20p-6s+23824+29q+23z+34q', '42s+71v-15t-85u-16w-57x+78z+86y-46p-53x-87r-32y+74x-16q+8x=-2327+30z', '-45s-2729+52p+50t-86x+55z+34u-17y-106r-5602-79v+64w+47y+76q+8r=2781-12q+2s+31t+6s-29x+18s-26t'))
print(solve("x=4y", "2x=8y", "x+y=5"))