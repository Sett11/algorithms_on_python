def count_way(a):
    m,n=len(a),len(a[0])
    a[0]=[1]*n
    for i in range(1,m):
        a[i][0]=1
    for i in range(1,m):
        for j in range(1,n):
            a[i][j]=a[i-1][j]+a[i][j-1]+a[i-1][j-1]
    return a


print(count_way([[0 for i in range(7)] for j in range(7)]))