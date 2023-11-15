def generate_chess_grafh():
    letters,numbers='abcdefgh','12345678'
    g={i+j:set() for i in letters for j in numbers}
    add_g=lambda e,c:g[e].add(c) and g[c].add(e)

    for i in range(8):
        for j in range(8):
            v1=letters[i]+numbers[j]
            if 0<=i+2<8 and 0<=j+1<8:
                v2=letters[i+2]+numbers[j+1]
                add_g(v1,v2)
            if 0<=i-2<8 and 0<=j+1<8:
                v2=letters[i-2]+numbers[j+1]
                add_g(v1,v2)
            if 0<=i+1<8 and 0<=j+2<8:
                v2=letters[i+1]+numbers[j+2]
                add_g(v1,v2)
            if 0<=i-1<8 and 0<=j+2<8:
                v2=letters[i-1]+numbers[j+2]
                add_g(v1,v2)
    return g