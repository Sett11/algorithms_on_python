def perm_str(a):
    l=len(a)
    if l==1:
        return a
    t=perm_str(a[1:])
    p=a[0]
    r=[]
    for i in t:
        for j in range(l):
            q=i
            r+=[q[0:j]+p+q[j:]]
    return r

print(perm_str('ABXDEFG'))