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



class Deque:
    def __init__(self,deque=[]):
        self.deque=deque
        self.size=len(deque)
        self.pointer_left=0
        self.pointer_right=self.size-1
    
    def push(self,v):
        self.deque.append(v)
        self.size+=1
        self.pointer_right+=1
    
    def pop_left(self):
        if self.pointer_left<=self.pointer_right:
            x=self.deque[self.pointer_left]
            self.deque[self.pointer_left]=0
            self.size-=1
            self.pointer_left+=1
            return x
        
    def pop_right(self):
        if self.pointer_right>=self.pointer_left:
            self.size-=1
            self.pointer_right-=1
            return self.deque.pop()
        
    def peek_left(self):
        if self.size:
            return self.deque[self.pointer_left]
    
    def peek_right(self):
        if self.size:
            return self.deque[self.pointer_right]
        
q=Deque()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.push(5)
print(q.pop_left(),q.peek_left(),q.pop_right(),q.peek_right(),q.pop_left(),q.pop_right(),q.pop_left(),q.push(9),q.peek_right())