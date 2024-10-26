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



from collections import namedtuple
from copy import deepcopy

Blob=namedtuple('Blob','x y size')

class Blobservation:
    def __init__(self,h,w=None):
        self.h=h
        self.w=w or h
        self._min=1e9
        self._mat=[[0]*self.w for _ in range(self.h)]
        self._board=deepcopy(self._mat)
    
    def _check(self,a):
        for i in a:
            try:
                b,c,d=i.values()
                if b<0 or b>=self.h or c<0 or c>=self.w or d<1 or d>21 or bool([j for j in i.values() if type(j)!=int]):
                    return False
            except:
                return False
        return True
    
    def populate(self,a):
        if not self._check(a):
            raise Exception('Is not valid populate!')
        for i in a:
            x,y,z=i['x'],i['y'],i['size']
            self._board[x][y]+=z
            self._min=min(self._min,self._board[x][y])


    def print_state(self):
        r,m=[],1e9
        for i in range(self.h):
            for j in range(self.w):
                if self._board[i][j]:
                    m=min(m,self._board[i][j])
                    r.append([i,j,self._board[i][j]])
        self._min=m
        return sorted(r,key=lambda x:(x[0],x[1]))
    
    def _next_step(self,curr,a):
        if not a:
            return curr.x,curr.y,0

        def hand(a,b):
            s=max(abs(a.x-b.x),abs(a.y-b.y))
            if s==1:
                return b.x,b.y,b.size
            if a.x==b.x:
                if a.y<b.y:
                    return a.x,a.y+1,0
                else:
                    return a.x,a.y-1,0
            if a.y==b.y:
                if a.x<b.x:
                    return a.x+1,a.y,0
                else:
                    return a.x-1,a.y,0
            if a.x<b.x and a.y<b.y:
                return a.x+1,a.y+1,0
            if a.x>b.x and a.y>b.y:
                return a.x-1,a.y-1,0
            if a.x<b.x and a.y>b.y:
                return a.x+1,a.y-1,0
            if a.x>b.x and a.y<b.y:
                return a.x-1,a.y+1,0
            
        if len(a)==1:
            return hand(curr,a[0])
        m=max(a,key=lambda e:e.size).size
        a=[i for i in a if i.size==m]
        if len(a)==1:
            return hand(curr,a[0])
        b=sorted([i for i in a if i.x<=curr.x and i.y>=curr.y],key=lambda e:(e.x,e.y))
        if b:return hand(curr,b[0])
        b=sorted([i for i in a if i.x>=curr.x and i.y>=curr.y],key=lambda e:(e.x,-e.y))
        if b:return hand(curr,b[0])
        b=sorted([i for i in a if i.x>=curr.x and i.y<=curr.y],key=lambda e:(-e.x,-e.y))
        if b:return hand(curr,b[0])
        b=sorted([i for i in a if i.x<=curr.x and i.y<=curr.y],key=lambda e:(-e.x,-e.y))
        if b:return hand(curr,b[0])
        return 'What the fack!???'
    
    def move(self,n=1):
        if type(n)!=int or n<1:
            raise Exception('Not valid input!')
        k=0
        a=list(map(lambda x:Blob(*x),self.print_state()))
        while n:
            r={}
            if len(a)<=1:
                break
            k=1
            for i in a:
                r[i]=[]
                m=1e9
                if i.size!=self._min:
                    for j in a:
                        if j.size<i.size:
                            d=max(abs(i.x-j.x),abs(i.y-j.y))
                            m=min(m,d)
                            r[i].append([j,d])
                    r[i]=[k[0] for k in r[i] if k[1]==m]
            r,q,w={i:self._next_step(i,r[i]) for i in r},deepcopy(self._mat),{}
            for i in r:
                b,c,_=r[i]
                d=i.size
                t=b,c
                q[b][c]+=d
                if t not in w:
                    w[t]=0
                w[t]+=d
            a=[Blob(*(list(i)+[w[i]])) for i in w]
            n-=1
        if k:
            self._board=q

b=Blobservation(10,9)
b.populate([{'x': 6, 'y': 6, 'size': 16}, {'x': 1, 'y': 6, 'size': 16}, {'x': 6, 'y': 3, 'size': 2}, {'x': 1, 'y': 4, 'size': 4}, {'x': 5, 'y': 1, 'size': 5}, {'x': 1, 'y': 8, 'size': 11}, {'x': 1, 'y': 1, 'size': 12}, {'x': 9, 'y': 0, 'size': 13}, {'x': 2, 'y': 3, 'size': 2}, {'x': 1, 'y': 0, 'size': 11}, {'x': 5, 'y': 7, 'size': 14}, {'x': 5, 'y': 2, 'size': 20}, {'x': 6, 'y': 1, 'size': 17}, {'x': 8, 'y': 4, 'size': 16}])
print(b.move(6))
print(b.move(2))
print(b.move(1992))
print(b.print_state())