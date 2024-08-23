import gmpy2
import inspect
import networkx as nx
import matplotlib.pyplot as plt
import re
from math import ceil,inf
from collections import defaultdict,deque,Counter
from string import ascii_uppercase,digits
from gen_graph import matrix,dfs_a,dfs_b,seq,seq_b,generate_chess_knight_grafh,p_graph as g,d_graph as dg,f_grapf as fg, ff_g,exp,exp_dict,net_g,options,back
from functools import reduce
from itertools import product,zip_longest
from copy import deepcopy
from operator import mul,add,sub,truediv
from random import shuffle,choice#,randint
q=list(range(1,1503))
shuffle(q)

class SudokuState:
  def __init__(self, grid):
    self.grid=grid
    self._children=[]
    self._min_choice=None

  def __eq__(self,other):
    return self.grid==other.grid

  def __ne__(self,other):
    return self.grid!=other.grid

  def poss_by_i(self,i,_):
    poss=set(range(1,10))
    for n in self.grid[i]:
      if n!=0:
        poss.remove(n)
    return poss

  def poss_by_j(self,i,j):
    poss=set(range(1,10))
    for i in self.grid:
      if i[j]!=0:
        poss.remove(i[j])
    return poss

  def poss_by_square(self,i,j):
    poss=set(range(1,10))
    sq_i=(i//3)*3
    sq_j=(j//3)*3
    for r in range(sq_i,sq_i+3):
      for c in range(sq_j,sq_j+3):
        n=self.grid[r][c]
        if n!=0:
          poss.remove(n)
    return poss

  def all_poss(self,i,j):
    i_poss=self.poss_by_i(i,j)
    j_poss=self.poss_by_j(i,j)
    sq_poss=self.poss_by_square(i,j)
    return i_poss.intersection(j_poss,sq_poss)

  @property
  def min_choice(self):
    if not self._min_choice:
      min_poss=10
      for i in range(9):
        for j in range(9):
          if self.grid[i][j]==0:
            n_poss=len(self.all_poss(i,j))
            if n_poss<min_poss:
              min_poss=n_poss
              self._min_choice=(i,j)
              if n_poss==1:
                return self._min_choice
    return self._min_choice

  @property
  def children(self):
    if not self._children:
      i,j=self.min_choice
      poss=self.all_poss(i,j)
      for p in poss:
        new_grid=deepcopy(self.grid)
        new_grid[i][j]=p
        child=SudokuState(new_grid)
        self._children.append(child)
    return self._children

  @property
  def is_goal(self):
    for i in self.grid:
      for n in i:
        if n==0:
          return False
    return True

def solve(g):
  start=SudokuState(g)
  a,b,c,r=deque([start]),deque([start]),deque(),start
  while b:
    if r.is_goal:
      return r.grid
    ch=[i for i in r.children if i not in c and i not in b and i not in a]
    if not ch:
      while a and r==a[0]:
        c.appendleft(r),a.popleft(),b.popleft()
        if b:
          r=b[0]
      a.appendleft(r)
    else:
      b.extendleft(ch)
      r=b[0]
      a.appendleft(r)

print(solve([
            [9, 0, 0, 0, 8, 0, 0, 0, 1],
            [0, 0, 0, 4, 0, 6, 0, 0, 0],
            [0, 0, 5, 0, 7, 0, 3, 0, 0],
            [0, 6, 0, 0, 0, 0, 0, 4, 0],
            [4, 0, 1, 0, 6, 0, 5, 0, 8],
            [0, 9, 0, 0, 0, 0, 0, 2, 0],
            [0, 0, 7, 0, 3, 0, 2, 0, 0],
            [0, 0, 0, 7, 0, 5, 0, 0, 0],
            [1, 0, 0, 0, 4, 0, 0, 0, 7]
        ]))