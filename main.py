from random import shuffle,choice#,randint
from re import sub
from math import ceil, inf
from collections import defaultdict, deque
from string import ascii_uppercase,digits
from gen_graph import matrix, dfs_a, dfs_b, seq, generate_chess_knight_grafh, p_graph as g, d_graph as dg
from pprint import pprint

def find_longest_substring_bracket(s):
    stask,m=[-1],0
    for i,j in enumerate(s):
        if j=='(':
            stask.append(i)
        else:
            stask.pop()
            if stask:m=max(m,i-stask[-1])
            else:
                stask.append(i)
    return m

pprint(find_longest_substring_bracket(')(())()()'),width=50,indent=3)