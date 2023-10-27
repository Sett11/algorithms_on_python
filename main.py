def prod(*a):
    return {()} if not a else [tuple([i]+list(j)) for i in a[0] for j in prod(*a[1:])]
    

print(prod({1},{2,3},{4,5,6},{7,8,9}))