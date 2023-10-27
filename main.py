def longest_common_subsequence(a,b):
    n,m=len(a),len(b)
    r=[[0]*(m+1) for i in range(n+1)]
    s=0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if a[i-1]==b[j-1]:
                r[i][j]=1+r[i-1][j-1]
            else:
                r[i][j]=max(r[i-1][j],r[i][j-1])
            s=max(s,r[i][j])
    return s

print(longest_common_subsequence('abcde','ace'))
print(longest_common_subsequence([1,2,3,4,4,4,4,5,6,7],[0,3,4,4,4,4,4,7,6]))