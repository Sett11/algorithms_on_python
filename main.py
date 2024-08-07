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

def f(wt,val,w):
    dp,n=[0]*(w+1),len(wt)
    for i in range(1,n+1):
        for j in range(w,0,-1):
            if wt[i-1]<=j:
                dp[j]=max(dp[j],dp[j-wt[i-1]]+val[i-1])
    return dp[w]

print(f([2,2,6,5,4],[6,3,5,4,6],10))