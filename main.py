from re import sub
from math import ceil, inf
from collections import defaultdict, deque, Counter
from string import ascii_uppercase, digits
from gen_graph import matrix, dfs_a, dfs_b, seq, seq_b, generate_chess_knight_grafh, p_graph as g, d_graph as dg, f_grapf as fg, ff_g
from functools import reduce
from itertools import product
from operator import mul,add,sub,truediv
from random import shuffle,choice#,randint
q=list(range(1,1503))
shuffle(q)


class Node:
    def __init__(self,data=None,parent=None,left=None,right=None):
        self.data=data
        self.parent=parent
        self.left=left
        self.right=right


def f(s):
    h=c=Node()
    for i in s:
        if i=='(':
            c.left=Node(parent=c)
            c=c.left
        elif i==')':
            c=c.parent
        elif i in '+-*/':
            c.data=i
            c.right=Node(parent=c)
            c=c.right
        else:
            c.data=int(i)
            c=c.parent
    return h

def ev(h):
    ops={'-':sub,'+':add,'*':mul,'/':truediv}
    l,r=h.left,h.right
    return ops[h.data](ev(l),ev(r)) if l and r else h.data

print(ev(f('((7+3)*(((5-2)+2)*3))')))