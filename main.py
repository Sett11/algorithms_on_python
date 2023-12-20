from random import shuffle,choice#,randint
from re import sub
from math import ceil,inf
from collections import defaultdict,deque
from string import ascii_uppercase
from gen_graph import p_graph as g


from random import randint

def f(a,s):
    n,r=len(a),set()
    for i in range(1,2**n+1):
        t,p=[],1
        for j in range(n):
            if i&p:
                t.append(a[j])
                if sum(t)>s:
                    break
            p*=2
        if sum(t)==s:
            r.add(tuple(sorted(t)))
    return r


print(f(sorted(randint(1,101) for i in range(20)),78))