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


class Stack:
    def __init__(self,stack=[]):
        self.stack=stack
        self.size=len(stack)
    
    def push(self,v):
        self.stack.append(v)
        self.size+=1
    
    def pop(self):
        self.size-=1
        return self.stack.pop()
    
    def is_empty(self):
        return not self.stack
    
    def peek(self):
        return self.stack[-1] if not self.is_empty() else None
    
s=Stack()
s.push(2)
s.push(3)
print(s.peek(),s.pop(),s.size)