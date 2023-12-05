from collections import defaultdict

def longest_arithSeq_length(self,a):
    o=defaultdict(dict)
    c=1

    for i in range(len(a)):
        for j in range(i):
            n=a[i]-a[j]
            if n not in o[j]:
                o[j][n]=1
            if n not in o[i]:
                o[i][n]=0
            o[i][n]=o[j][n]+1
            c=max(c,o[i][n])

    return c

print(longest_arithSeq_length([9,4,7,2,10]))