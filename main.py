from random import shuffle,choice#,randint
from re import sub
from math import ceil, inf
from collections import defaultdict, deque
from string import ascii_uppercase
from gen_graph import matrix, dfs_a, dfs_b, generate_chess_knight_grafh, p_graph as g, d_graph as dg

n,m=map(int,input().split())
a,r=list(range(n*m,0,-1)),[[0]*m for _ in range(n)]
for i in range(n+m-1):
    k,j=0 if i<m else i-m+1,i if i<m else m-1
    while k<n and j>=0:
        r[k][j]=a.pop()
        k+=1
        j-=1
for i in r:
    print(' '.join(map(lambda x:str(x).ljust(3),i)))