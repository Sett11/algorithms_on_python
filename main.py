def longestIncreasingPath(a):
    n,m=len(a),len(a[0])
    r=[]

    def dfs(i,j,w,c):
        if i<0 or i>=n or j<0 or j>=m or a[i][j]<=w:
            r.append(c)
            return
        dfs(i+1,j,a[i][j],c+1)
        dfs(i-1,j,a[i][j],c+1)
        dfs(i,j+1,a[i][j],c+1)
        dfs(i,j-1,a[i][j],c+1)

    for i in range(n):
        for j in range(m):
            dfs(i,j,-1,0)
            if n in a:
                break

    return max(r)


print(longestIncreasingPath([[3,4,5],
           [3,2,6],
           [2,2,1]]))