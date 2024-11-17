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



dist=lambda a,b:((b[0]-a[0])**2+(b[1]-a[1])**2)**.5

def over_kill(a,l,r):
    md,mp=float('inf'),None
    for i in range(l,r):
        for j in range(i+1,r):
            p=(a[i],a[j])
            d=dist(*p)
            if d<md:
                md,mp=d,p
    return mp

def cpr(a,l,r):
    if r-l<4:
        return over_kill(a,l,r)
    m=(l+r)//2
    lp,rp=cpr(a,l,m),cpr(a,m,r)
    p=min(lp,rp,key=lambda x:dist(*x))
    ml=(a[m][0]+a[m+1][0])/2
    mp=[i for i in a[l:r] if abs(i[0]-ml)<dist(*p)]
    l=len(mp)
    mp.sort(key=lambda x:x[1])
    for i in range(l):
        for j in range(i+1,min(i+4,l)):
            k=(mp[i],mp[j])
            p=min(p,k,key=lambda x:dist(*x))
    return p

def closest_pair(a):
    return cpr(sorted(a),0,len(a))

print(closest_pair(((9689.556163781199, -10881.605736237032), (14363.64143623233, -11945.80372534414), (9590.807563444518, -8381.042024829681), (6219.468264163184, -12711.165469088719), (13623.64165661393, -14156.145930879396), (12237.539010850962, -11001.494701798867), (8284.294036249867, -9442.52289980639), (11801.675965031054, -13947.220079651703), (8639.740154457884, -13010.870678420775), (10039.877865574796, -15074.33903310707), (12353.083966572198, -14856.60186186019), (7177.300417323691, -14096.349494266098), (12127.828331870714, -9004.750232326269), (12490.097362838716, -12508.608305440317), (8731.32859606089, -15213.694532448717), (12196.074564485307, -11006.599792613673), (9394.092421102316, -17230.31656852788), (15452.813870715512, -12933.397857186577), (11231.640944180612, -7448.969559297799), (10628.450086733917, -9581.330049999786), (5332.335534387627, -11163.138616208507), (8341.440245571172, -11461.076049304054), (10874.413814298663, -12469.86564672788), (11446.314171199283, -16298.95567622374), (13442.13860258231, -10498.202782173303), (6687.888954355447, -10456.507685549379))))