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


def calculate(s):
    stack=[]
    for i in s.split()[::-1]:
        if re.sub(r'[-.]','',i).isdigit():
            stack.append(float(i))
        else:
            stack.append(eval(f'{stack.pop()}{i}{stack.pop()}'))
    return stack[-1]

print(calculate('/ + 3 5 * 2 2'))