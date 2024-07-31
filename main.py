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


class PrefixTree:
    def __init__(self,key=None,parent=None):
        self.key=key
        self.parent=parent
        self.children={}
        self.end=False
    
    def get_word(self):
        r,h=[],self
        if h is not None:
            r.insert(0,h.key)
            h=h.parent
        return ''.join(r)
    
    def contain(self,s):
        h=self
        for i in s:
            if i in h.children:
                h=h.children[i]
            else:
                return False
        return h.end
    
    def insert(self,s):
        h=self
        for i in s:
            if i not in h.children:
                h.children[i]=PrefixTree(i,h)
            h=h.children[i]
        h.end=True

    def remove(self,s):
        h=self
        def find_word(h,s,i):
            if i==len(s):
                if not h.end:
                    return False
                h.end=False
                return len(h.children)==0
            if find_word(h.children[s[i]],s,i+1):
                del h.children[s[i]]
                return not h.end and len(h.children)==0
            return False
        find_word(h,s,0)

    def __repr__(self):
        return str(self.children)

p=PrefixTree()
p.insert('Hell')
p.insert('Hello')
print(p.contain('Hello'),p.contain('Hell'))
p.insert('World')
p.remove('Hell')
print(p.contain('Hell'))
print(repr(p))