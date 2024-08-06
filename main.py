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

def knapsack(items,n):
    dp = [(0, []) for _ in range(n+1)]
    for item in items:
        for w in range(n, 0, -1):
            if item[0] <= w:
                x, y = dp[w-item[0]]
                if x + item[1] > dp[w][0]:
                    dp[w] = (x+item[1], y+[item])
    return dp[n][1]

print(knapsack([(2,6),(2,3),(6,5),(5,4),(4,6)],10))