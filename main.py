from math import inf
from gen_graph import p_graph

def get_min(R,U):
    rm=(inf,'Z','Z')

    for v in U:
        rr=min(R,key=lambda x: x[0] if (x[1]==v or x[2]==v) and (x[1] not in U or x[2] not in U) else inf)
        if rm[0]>rr[0]:
            rm=rr
    
    return rm

def prim(a):
    s=list(set(''.join([i[1]+i[2] for i in a])))
    n=len(s)
    a=[(inf,'Z','Z')]+a
    u={s[0]}
    r=[]

    while len(u)<n:
        m=get_min(a,u)
        if m[0]==inf:
            break
        r.append(m)
        u.update([m[1],m[2]])

    return r


print(prim(p_graph))