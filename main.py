import gmpy2
import inspect
import networkx as nx
import matplotlib.pyplot as plt
import re
from math import ceil,inf,factorial
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

class Sudoku:
   def __init__(self,a):
      self.a=a
      self._min=None
      self._childrens=[]

   def get_i(self,i):
      p=set(range(1,10))
      for j in self.a[i]:
         if j:
            p.remove(j)
      return p
   
   def get_j(self,j):
      p=set(range(1,10))
      for i in self.a:
         if i[j]:
            p.remove(i[j])
      return p
   
   def get_sq(self,i,j):
      p=set(range(1,10))
      i,j=i//3*3,j//3*3
      for k in range(i,i+3):
         for c in range(j,j+3):
            if self.a[k][c]:
               p.remove(self.a[k][c])
      return p
   
   def get_all(self,i,j):
      return self.get_i(i).intersection(self.get_j(j),self.get_sq(i,j))
   
   @property
   def get_min(self):
      if not self._min:
         m=10
         for i in range(9):
            for j in range(9):
               if self.a[i][j]==0:
                  n=len(self.get_all(i,j))
                  if n<m:
                     m=n
                     self._min=(i,j)
                     if n==1:
                        return self._min
      return self._min
   
   @property
   def get_child(self):
      if not self._childrens:
         i,j=self.get_min
         for k in self.get_all(i,j):
            n=deepcopy(self.a)
            n[i][j]=k
            self._childrens.append(Sudoku(n))
      return self._childrens
   
   @property
   def check(self):
      for i in self.a:
         for j in i:
            if j==0:
               return False
      return True
   

def f(g):
   s=Sudoku(g)
   a,b,c,r=deque([s]),deque([s]),deque(),s
   while b:
      if r.check:
         return r.a
      ch=[i for i in r.get_child if i not in a and i not in b and i not in c]
      if not ch:
         while a and a[0]==r:
            c.appendleft(r),b.popleft(),a.popleft()
            if b:
               r=b[0]
         a.appendleft(r)
      else:
         b.extendleft(ch)
         r=b[0]
         a.appendleft(r)

print(f(sudoku))