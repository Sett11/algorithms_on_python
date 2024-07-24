from re import sub
from math import ceil, inf
from collections import defaultdict, deque, Counter
from string import ascii_uppercase, digits
from gen_graph import matrix,dfs_a,dfs_b,seq,seq_b,generate_chess_knight_grafh,p_graph as g,d_graph as dg,f_grapf as fg, ff_g,exp
from functools import reduce
from itertools import product
from operator import mul,add,sub,truediv
from random import shuffle,choice#,randint
q=list(range(1,1503))
shuffle(q)


class Node:
    def __init__(self,val=None,previous=None,next=None):
        self.val=val
        self.previous=previous
        self.next=next

class LinkedList:
    def __init__(self,head=None,tail=None,size=0):
        self.head=head
        self.tail=tail
        self.size=size
    
    def add_left(self,v):
        if self.head is None:
            self.head=self.tail=Node(v)
        else:
            h=Node(v,previous=None,next=self.head)
            self.head.previous=self.head=h
        self.size+=1
    
    def add_right(self,v):
        if self.tail is None:
            self.tail=self.head=Node(v)
        else:
            h=Node(v,previous=self.tail)
            self.tail.next=self.tail=h
        self.size+=1
    
    def pop_left(self):
        if self.head is None:
            return
        x=self.head.val
        if self.head==self.tail:
            self.head=self.tail=None
        else:
            self.head=self.head.next
            self.head.previous=None
        self.size-=1
        return x
    
    def pop_right(self):
        if self.tail is None:
            return
        x=self.tail.val
        if self.head==self.tail:
            self.head=self.tail=None
        else:
            self.tail=self.tail.previous
            self.tail.next=None
        self.size-=1
        return x
    
    def __contains__(self,v):
        h=self.head
        while h:
            if h.val==v:
                return True
            h=h.next
        return False
    
    def __iter__(self):
        h=self.head
        while h:
            yield h.val
            h=h.next
    
    def __repr__(self):
        r,h=[],self.head
        while h:
            r.append(h.val)
            h=h.next
        return ' -> '.join(map(str,r))
    
l=LinkedList()
l.add_left(1)
l.add_left(2)
l.add_left(3)
l.add_right(4)
print([i for i in l],l.size)
print(3 in l,l.pop_left(),l.pop_right())
print(repr(l),l.size)