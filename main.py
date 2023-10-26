def generate_permutations(n,m,p=None):
    if not m:
        print(p)
        return
    p=p or []
    for i in range(n):
        p.append(i)
        generate_permutations(n,m-1,p)
        p.pop()

generate_permutations(2,4)