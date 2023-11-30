def manaker_palindrom(s):
    t='#'.join('^{}$'.format(s))
    n=len(t)
    p=[0]*n
    c=r=0

    for i in range(1,n-1):
        p[i]=(r>i) and min(r-i,p[2*c-i])
        while t[i+1+p[i]]==t[i-1-p[i]]:
            p[i]+=1
        if i+p[i]>r:
            c,r=i,i+p[i]

    x,y=max((i,j) for j,i in enumerate(p))

    return s[(y-x)//2:(x+y)//2]


print(manaker_palindrom('jddddjuudjjjdjjjuuudujuudjjjjujdduujduujjujdudjjuuuuuddjjjddddjdj'))
print(manaker_palindrom('ttaaftffftfaafatf'))