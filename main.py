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
    def __init__(self,items=[],size=0):
        self.items=items
        self.size=size

    def add(self,v):
        self.size+=1
        self.items.append(v)
    
    def pop_right(self):
        self.size-=1
        return self.items.pop()
    
class Queue(Stack):
    def __init__(self):
        super().__init__()
        self.pointer=0
    
    def pop_left(self):
        if self.size:
            x=self.items[self.pointer]
            self.items[self.pointer]=0
            self.size-=1
            self.pointer+=1
            return x
        
class Deque(Queue,Stack):
    def __init__(self):
        super().__init__()

q=Deque()
q.add(1)
q.add(2)
q.add(3)
q.add(4)
q.add(5)
print(q.pop_right(),q.pop_left(),q.size)