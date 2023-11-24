def matrix_product(a,b):
    if len(a[0])==len(b):
        return [[sum(a[i][j]*b[j][k] for j in range(len(b))) for k in range(len(b[0]))] for i in range(len(a))]
    

print(matrix_product([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
print(matrix_product([[0.5, 1],[1.5, 2]], [[0.2, 0.4], [0.6, 0.8]]))