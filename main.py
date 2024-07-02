from re import sub
from math import ceil, inf
from collections import defaultdict, deque, Counter
from string import ascii_uppercase,digits
from gen_graph import matrix, dfs_a, dfs_b, seq, seq_b, generate_chess_knight_grafh, p_graph as g, d_graph as dg, f_grapf as fg, ff_g
from pprint import pprint
from functools import lru_cache,reduce
from itertools import product
from operator import mul
from random import shuffle,choice#,randint


def get_max_vertex(k,a,s):
    m,v=0,-1
    for i,j in enumerate(a[k]):
        if i in s:
            continue
        if j[2]==1:
            if m<j[0]:
                m=j[0]
                v=i
        else:
            if m<j[1]:
                m=j[1]
                v=i
    return v

def get_max_flow(t):
    return min(*[x[0] for x in t])

def updateV(v,t,f):
    for i in t:
        if i[1]==-1:
            continue
        sgn=v[i[2]][i[1]][2]
        v[i[1]][i[2]][0]-=f*sgn
        v[i[1]][i[2]][1]+=f*sgn
        v[i[2]][i[1]][0]-=f*sgn
        v[i[2]][i[1]][1]+=f*sgn

def ford_fulkerson(a,init,end):
    tinit=(inf,-1,init)
    f=[]
    j=init
    while j!=-1:
        k=init
        t=[tinit]
        s={init}
        while k!=end:
            j=get_max_vertex(k,a,s)
            if j==-1:
                if k==init:
                    break
                else:
                    k=t.pop()[2]
                    continue
            c=a[k][j][0] if a[k][j][2]==1 else a[k][j][1]
            t.append((c,j,k))
            s.add(j)
            if j==end:
                f.append(get_max_flow(t))
                updateV(a,t,f[-1])
                break
            k=j
    return sum(f)


print(ford_fulkerson(ff_g,0,4))