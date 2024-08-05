import gmpy2
import inspect
import re
from math import ceil, inf
from collections import defaultdict, deque, Counter
from string import ascii_uppercase, digits
from gen_graph import matrix,dfs_a,dfs_b,seq,seq_b,generate_chess_knight_grafh,p_graph as g,d_graph as dg,f_grapf as fg, ff_g,exp,exp_dict,LazyInit
from functools import reduce
from itertools import product
from operator import mul,add,sub,truediv
from random import shuffle,choice#,randint
q=list(range(1,1503))
shuffle(q)

class HashTable:
    def __init__(self,size):
        self.size=size
        self.keys=[None]*size
        self.values=[None]*size
    
    def _put_(self,k,v):
        h=self._hashing_(k)
        if self.keys[h] is None:
            self.keys[h]=k
            self.values[h]=v
        else:
            if self.keys[h]==k:
                self.values[h]=v
            else:
                while self.keys[h] is not None and self.keys[h]!=k:
                    h=self._rehashing_(h)
                if self.keys[h] is None:
                    self.keys[h]=k
                    self.keys[h]=v
                else:
                    self.values[h]=v

    def _hashing_(self,v):
        c=str(v**2)
        n=len(c)
        x=int(n%2==0)
        return int(c[n//2-x:n//2+x] if x else c[n//2])%self.size

    def rehashing(self,v):
        return (v+1)%self.size

    def _get_(self,k):
        s=self._hashing_(k)
        data=None
        stop=found=False
        position=s
        while self.keys[position] is not None and not found and not stop:
            if self.keys[position]==k:
                found=True
                data=self.values[position]
            else:
                position=self._rehashing_(position)
                if position==s:
                    stop=True
        return data
    
    def __getitem__(self,k):
        return self._get_(k)
    
    def __setitem__(self,k,v):
        return self._put_(k,v)

H=HashTable(97)
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"

print(H[20])

print(H[17])
H[20]='duck'
print(H[20])