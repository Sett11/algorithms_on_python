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

class Segment_tree:
    def __init__(self,a,op):
        self.a=a
        self.op=op
        self.n=len(a)
        self.tree=[None]*(self.n*4)
        self.build_tree(self.a,0,0,self.n-1)
    
    def build_tree(self,a,n,l,r):
        if l==r:
            self.tree[n]=a[l]
        else:
            m=(l+r)//2
            self.build_tree(a,2*n+1,l,m)
            self.build_tree(a,2*n+2,m+1,r)
            self.tree[n]=self.op(self.tree[2*n+1],self.tree[2*n+2])

    def get_res(self,l,r,n=0,nl=0,nr=None):
        if l<=nl and r>=nr:
            return self.tree[n]
        if r<nl or l>nr:
            return
        m=(nl+nr)//2
        left_res=self.get_res(l,r,2*n+1,nl,m)
        right_res=self.get_res(l,r,2*n+2,m+1,nr)
        if left_res is None:
            return right_res
        if right_res is None:
            return left_res
        return self.op(left_res,right_res)

def compute_ranges(a,op,r):
    t,n=Segment_tree(a,op),len(a)
    return [t.get_res(i[0],i[1]-1,nr=n-1) for i in r]

def _sum(a,b): 
    return a+b

def _max(a,b): 
    return a if a > b else b

def _gcd(a,b): 
    return a if b == 0 else _gcd(b, a%b)

def _lcm(a,b): 
    if a == 0: return b
    if b == 0: return a
    return a*b / _gcd(a,b)

print(compute_ranges([1, 5, 8, 5, 1, 8], _sum, [[0, 4], [0, 6], [2, 4], [1, 4]]))
print(compute_ranges([2, 4, 9, 1, 1, 14, 7], _max, [[0, 2], [2, 7], [1, 4], [4, 5], [5, 7], [2, 5]]))
print(compute_ranges([0, 0, 4, 75, 12, 0, 16, 5], _gcd, [[1, 4], [2, 6], [0, 1], [1, 4], [4, 7]]))