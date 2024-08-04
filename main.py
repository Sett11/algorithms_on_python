import gmpy2
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

def sieve_eratosthenes(n):
    limit=gmpy2.isqrt(n)+1
    n+=1
    bitmap=gmpy2.xmpz(3)
    bitmap[4:n:2]=-1
    for i in bitmap.iter_clear(3,limit):
        bitmap[i*i:n:i+i]=-1
    return list(bitmap.iter_clear(2,n))

print(sieve_eratosthenes(10000))