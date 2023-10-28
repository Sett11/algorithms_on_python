def count_way(a):
    n,m=len(a),len(a[0])
    a[0]=[1]*m
    for i in range(n):
        a[i][0]=1
    for i in range(1,n):
        for j in range(1,m):
            a[i][j]=a[i-1][j]+a[i][j-1]
    return a

def diagonals(a):
    r=[]
    q=[]
    v=2
    while v:
        for i in range(len(a)-(0 if v==2 else 1)):
            k=i
            j=0
            t=[]
            while k>=0 and j<len(a[0]):
                t.append(a[j][k])
                j+=1
                k-=1
            if v==2:
                r.append(t)
            else:
                q.insert(0,t)
        v-=1
        a=[p[::-1] for p in a][::-1]
    return r+q

print(diagonals(count_way([[0]*5 for _ in range(5)])))