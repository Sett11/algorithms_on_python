import re
from math import ceil, inf
from collections import defaultdict, deque, Counter
from string import ascii_uppercase, digits
from gen_graph import matrix,dfs_a,dfs_b,seq,seq_b,generate_chess_knight_grafh,p_graph as g,d_graph as dg,f_grapf as fg, ff_g,exp,exp_dict
from functools import reduce
from itertools import product
from operator import mul,add,sub,truediv
from random import shuffle,choice#,randint
q=list(range(1,1503))
shuffle(q)


class BinHeap:
    def __init__(self,heap_list=[0],size=0):
        self.heap_list=heap_list
        self.size=size

    def pers_up(self,i):
        while i//2:
            if self.heap_list[i]<self.heap_list[i//2]:
                self.heap_list[i],self.heap_list[i//2]=self.heap_list[i//2],self.heap_list[i]
            i//=2
    
    def insert(self,v):
        self.heap_list.append(v)
        self.size+=1
        self.pers_up(self.size)

    def pers_down(self,i):
        while i*2<self.size:
            m=self.min_child(i)
            if self.heap_list[i]>self.heap_list[m]:
                self.heap_list[i],self.heap_list[m]=self.heap_list[m],self.heap_list[i]
            i=m

    def min_child(self,i):
        if i*2+1>self.size or self.heap_list[i*2]<self.heap_list[i*2+1]:
            return i*2
        return i*2+1
    
    def del_min(self):
        x=self.heap_list[1]
        self.heap_list[1]=self.size-1
        self.size-=1
        self.heap_list.pop()
        self.pers_down(1)
        return x
    
    def build_heap(self,a):
        n=len(a)
        i,self.size=n//2,n
        self.heap_list=[0]+a[:]
        while i:
            self.pers_down(i)
            i-=1

h=BinHeap()
h.build_heap([9,5,6,2,3])
print(h.heap_list)
print(h.del_min())
print(h.size)
h.insert(12)
print(h.heap_list)
h.insert(1)
print(h.heap_list,h.size)        