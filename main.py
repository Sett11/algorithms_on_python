def count_island(a):
    n=len(a)
    s=set()

    def dfs(i):
        if i not in s:
            s.add(i)
            for j in range(n):
                if a[i][j]:
                    dfs(j)

    c=0

    for i in range(n):
        if i not in s:
            dfs(i)
            c+=1

    return c

print(count_island([[1,1,0],[1,1,0],[0,0,1]]))