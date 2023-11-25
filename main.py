def d(m):
    if len(m)==1:
        return m[0][0]
    if len(m)==2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]
    return sum(((-1)**j)*v*d(f(m,0,j)) for j,v in enumerate(m[0]))

def f(m,x,y):
    return [[v for j,v in enumerate(r) if j!=y] for i,r in enumerate(m) if i!=x]


print(d([[8, -5, 9, -1, 6, 4], [-3, 5, 9, -10, 7, 7], [1, -2, -4, 7, -2, 3], [9, 4, -10, -3, -6, -1], [-2, -9, 6, 9, -4, 2], [4, -9, 10, 5, 0, 4]]))