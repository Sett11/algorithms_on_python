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


class Queue:
    def __init__(self,queue=[]):
        self.queue=queue
        self.size=len(queue)
        self.pointer=0

    def push(self,v):
        self.queue.append(v)
        self.size+=1
    
    def pop(self):
        if self.size:
            x=self.queue[self.pointer]
            self.queue[self.pointer]=0
            self.pointer+=1
            self.size-=1
            return x
    
    def peek(self):
        if self.size:
            return self.queue[self.pointer]
    
q=Queue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.push(5)

print(q.pop(),q.pop(),q.pop(),q.pop(),q.pop(),q.push(9),q.pop(),q.peek(),q.queue)