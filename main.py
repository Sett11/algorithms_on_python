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


def optimal_number_of_coins(n,a):
    r=[0]+[n+1]*n
    for i in range(1,n+1):
        for j in a:
            if j<=i:
                r[i]=min(r[i],r[i-j]+1)
    return -1 if r[n]>n else r[n]


print(optimal_number_of_coins(33,[1, 6, 9, 10]))