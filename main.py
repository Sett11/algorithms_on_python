from random import shuffle,choice#,randint
from re import sub
from math import ceil,inf
from collections import defaultdict,deque
from string import ascii_uppercase
from gen_graph import matrix


def mp(a,x,y):
    if [x,y]==[0,0]:
        return a[0][0]
    n,m=x+1,y+1
    r=[[0]*m for _ in range(n)]
    r[0][0]=a[0][0]
    for i in range(n):
        r[i][0]=r[i-1][0]+a[i][0]
    for i in range(m):
        r[0][i]=r[0][i-1]+a[0][i]
    for i in range(1,n):
        for j in range(1,m):
            r[i][j]=min(r[i-1][j],r[i][j-1])+a[i][j]
    return r[-1][-1]

print(mp(matrix,6,6))