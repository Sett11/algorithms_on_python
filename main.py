import gmpy2
import inspect
import networkx as nx
import matplotlib.pyplot as plt
import re
from math import ceil,inf,factorial
from collections import defaultdict,deque,Counter
from string import ascii_uppercase,digits
from gen_graph import matrix,dfs_a,dfs_b,seq,seq_b,generate_chess_knight_grafh,p_graph as g,d_graph as dg,f_grapf as fg, ff_g,exp,exp_dict,net_g,options,back,sudoku,kad
from functools import reduce
from itertools import product,zip_longest,permutations
from copy import deepcopy
from operator import mul,add,sub,truediv
from decimal import Decimal
from random import shuffle,choice#,randint
q=list(range(1,1503))
shuffle(q)
def fucken_indentations():
   ...

def solve_puzzle(a):
    n=len(a)//4
    res,p,rows,cols=[[0 for _ in range(n)] for __ in range(n)],list(permutations(range(n),n)),[],[]
    cl,cr=list(map(lambda x:count_steps(x,n),p)),list(map(lambda x:count_steps(x[::-1],n),p))
    for i in range(n):
        l,r=a[n*4-i-1],a[n+i]
        rows.append([p[i] for i in range(len(p)) if (l==0 or cl[i]==l) and (r==0 or cr[i]==r)])
    for i in range(n):
        l,r=a[i],a[n*3-i-1]
        cols.append([p[i] for i in range(len(p)) if (l==0 or cl[i]==l) and (r==0 or cr[i]==r)])
    while [len(i) for i in rows].count(1)<n:
        state=[len(i) for i in rows]+[len(i) for i in cols]
        try_solve(rows,cols,res,n)
        if [len(i) for i in rows].count(1)<n and [len(i) for i in rows]+[len(i) for i in cols]==state:
            heights_sort=sorted([(len(j),0,i) for i,j in enumerate(rows)]+[(len(j),1,i) for i,j in enumerate(cols)])
            v=False
            for height in heights_sort:
                if height[0]==1:
                    continue
                index=height[2]
                for i in range(height[0]):
                    c_rows,c_cols,c_puzzle=[i.copy() for i in rows],[i.copy() for i in cols],[i.copy() for i in res]
                    if height[1]==0:
                        c_rows[index]=[rows[index][i]]
                    else:
                        c_cols[index]=[cols[index][i]]
                    if not try_solve(c_rows,c_cols,c_puzzle,n):
                        if height[1]==0:
                            rows[index].pop(i)
                        else:
                            cols[index].pop(i)
                        v=True
                        break
                if v:
                    break
            if not v:    
                break
    return res

def count_steps(a,n):
    m=s=0
    for i in a:
        if i>=m:
            s+=1
            m=i
        if i>=n-1:
            break
    return s

def try_solve(rows,cols,puzzle,n):
    v=True
    while v:
        v=False
        for row in range(n):
            for col in range(n):
                count_cols=[len(hyp(cols[col],row,i))>0 for i in range(n)]
                count_rows=[len(hyp(rows[row],col,i))>0 for i in range(n)]
                if count_rows.count(True)==0 or count_cols.count(True)==0:
                    return False
                if count_rows.count(True)==1 or puzzle[row][col]==0:
                    puzzle[row][col]=count_rows.index(True)+1
                elif count_cols.count(True)==1 or puzzle[row][col]==0:
                    puzzle[row][col]=count_cols.index(True)+1
                for i in range(n):
                    if count_cols[i]==count_rows[i]:
                        continue
                    if count_cols[i]:
                        cols[col]=[r for r in cols[col] if r[row]!=i]
                    if count_rows[i]:
                        rows[row]=[c for c in rows[row] if c[col]!=i]
                    v=True
    return True    

def hyp(a,x,h):
    return [i[x] for i in a if i[x]==h]

print(solve_puzzle([7,0,0,0,2,2,3, 0,0,3,0,0,0,0, 3,0,3,0,0,5,0, 0,0,0,0,5,0,4]))