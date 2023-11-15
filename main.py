from collections import deque

g={'A':{'B':2,'H':15},
   'B':{'C':1,'D':5},
   'C':{'B':1,'D':3,'G':1,'F':2},
   'D':{'C':3,'F':4,'E':6},
   'G':{'C':1,'F':1},
   'F':{'C':2,'G':1,'D':4,'E':7,'H':3},
   'E':{'F':7,'D':6,'I':2},
   'I':{'E':2,'H':12},
   'H':{'A':15,'I':12}}

def dijcstra(s):
    q=deque([s])
    w={s:0}

    while q:
        v=q.popleft()
        for i in g[v]:
            t=w[v]+g[v][i]
            if i not in w or t<w[i]:
                w[i]=t
                q.appendleft(i)
    
    return w

def cheap_path_in_graph(s,e):
    m=dijcstra(s)
    r=[e]

    while r[-1]!=s:
        t=r[-1]
        n=m[t]
        p=[i for i in g[t] if n-g[t][i]==m[i]]
        if not p:
            break
        next=p[0]
        r.append(next)
        
    r.append(s)
    return r[::-1]

print(cheap_path_in_graph('A','I'))