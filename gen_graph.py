def generate_chess_knight_grafh():
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

def generate_chess_bishop_graph():
    letters='abcdefgh'
    numbers='12345678'
    g={i+j:set() for i in letters for j in numbers}
    add=lambda e,c:g[e].add(c) and g[c].add(e)

    for i in range(8):
        for j in range(8):
            v1=letters[i]+numbers[j]
            t=[[k,t] for k,t in [[i+1,j+1],[i-1,j-1],[i-1,j+1],[i+1,j-1]] if 0<=k<8 and 0<=t<8]
            for e,u in t:
                add(v1,letters[e]+numbers[u])
    
    return g

d_graph={'A':{'B':2,'H':15},
   'B':{'C':1,'D':5},
   'C':{'B':1,'D':3,'G':1,'F':2},
   'D':{'C':3,'F':4,'E':6},
   'G':{'C':1,'F':1},
   'F':{'C':2,'G':1,'D':4,'E':7,'H':3},
   'E':{'F':7,'D':6,'I':2},
   'I':{'E':2,'H':12},
   'H':{'A':15,'I':12}}