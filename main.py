from random import shuffle,choice#,randint
from re import sub
from math import ceil, inf
from collections import defaultdict, deque
from string import ascii_uppercase,digits
from gen_graph import matrix, dfs_a, dfs_b, seq, seq_b, generate_chess_knight_grafh, p_graph as g, d_graph as dg, k_graph as k
from pprint import pprint
import matplotlib.pyplot as plt


def kruckal(a):
    a=sorted(a)
    u,d,t=set(),{},[]
    for i in a:
        if i[1] not in u or i[2] not in u:
            if i[1] not in u and i[2] not in u:
                d[i[1]]=d[i[2]]=[i[1],i[2]]
            else:
                if not d.get(i[2]):
                    d[i[1]].append(i[2])
                    d[i[2]]=d[i[1]]
                else:
                    d[i[2]].append(i[1])
                    d[i[1]]=d[i[2]]
            t.append(i)
            u.update([i[1],i[2]])
    for i in a:
        if i[1] not in d[i[2]]:
            t.append(i)
            x=d[i[1]]
            d[i[1]]+=d[i[2]]
            d[i[2]]+=x
    return t

print(kruckal(g))