def levenshtein(a,b):
    n,m=len(a),len(b)
    r=[[i+j if i*j==0 else 0 for j in range(m+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if a[i-1]==b[j-1]:
                r[i][j]=r[i-1][j-1]
            else:
                r[i][j]=1+min(r[i-1][j],r[i][j-1],r[i-1][j-1])
    return r[-1][-1]


print(levenshtein('nayvyedosf', 'sjxen'))