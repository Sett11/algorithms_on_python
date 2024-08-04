from math import inf
from operator import mul,add,sub,truediv
import inspect

class LazyInit(type):
     @classmethod
     def lazi_init(msc,init):
          def wrap(*args):
               p=inspect.getfullargspec(init).args
               self=args[0]
               for i in range(1,len(args)):
                    setattr(self,p[i],args[i])
          return wrap
     
     def __new__(msc,name,bases,attrs):
          cls=type(name,bases,attrs)
          setattr(cls,'__init__',LazyInit.lazi_init(attrs['__init__']))
          return cls

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

def convert_array_to_graph(a):
    n,m=len(a),len(a[0])
    g={}

    for i in range(n):
        for j in range(m):
            x=(i,j)
            g[x]={}
            r=[[(t,k),a[t][k]] for t,k in [[i+1,j],[i-1,j],[i,j+1],[i,j-1],[i+1,j+1],[i-1,j-1],[i+1,j-1],[i-1,j+1]] if t>=0 and k>=0 and t<n and k<m]
            for b,c in r:
                g[x][b]=c+a[i][j]

    return g


def convert_two_dimensional_array_to_graph(a):
    r=set(sum(a,[]))
    g={i:set() for i in r}
    add=lambda e,c:g[e].add(c) and g[c].add(e)

    for i in r:
        for j in a:
            if i in j:
                add(i,[k for k in j if k!=i][0])
    
    return g


d_graph={'A':{'B':2,'H':15},
   'B':{'C':1,'D':5,'Z':5,'A':2},
   'C':{'B':1,'D':3,'G':1,'F':2},
   'D':{'C':3,'F':4,'E':6},
   'G':{'C':1,'F':1},
   'F':{'C':2,'G':1,'D':4,'E':7,'H':3},
   'E':{'F':7,'D':6,'I':2},
   'I':{'E':2,'H':12,'Z':2},
   'H':{'A':15,'I':12,'Z':7},
   'Z':{'H':7,'I':2,'B':5}}


p_graph=[[1, 'A', 'B'], [1, 'A', 'E'], [1, 'B', 'A'], [1, 'E', 'A'], [1, 'G', 'H'], [1, 'H', 'G'], [2, 'A', 'F'], [2, 'D', 'E'], [2, 'D', 'H'], [2, 'E', 'D'], [2, 'F', 'A'], [2, 'F', 'G'], [2, 'G', 'F'], [2, 'H', 'D'], [3, 'B', 'E'], [3, 'C', 'D'], [3, 'D', 'C'], [3, 'E', 'B'], [4, 'D', 'G'], [4, 'E', 'F'], [4, 'F', 'E'], [4, 'G', 'D'], [5, 'A', 'H'], [5, 'B', 'F'], [5, 'F', 'B'], [5, 'H', 'A'], [6, 'B', 'C'], [6, 'C', 'B'], [7, 'C', 'H'], [7, 'H', 'C'], [8, 'C', 'G'], [8, 'G', 'C']]
f_grapf=[[0, 2, inf, 3, 1, inf, inf, 10],
         [2, 0, 4, inf, inf, inf, inf, inf],
         [inf, 4, 0, inf, inf, inf, inf, 3],
         [3, inf, inf, 0, inf, inf, inf, 8],
         [1, inf, inf, inf, 0, 2, inf, inf],
         [inf, inf, inf, inf, 2, 0, 3, inf],
         [inf, inf, inf, inf, inf, 3, 0, 1],
         [10, inf, 3, 8, inf, inf, 1, 0],]

ff_g=[[[0,0,1], [20,0,1], [30,0,1], [10,0,1], [0,0,1]],
     [[20,0,-1], [0,0,1], [40,0,1], [0,0,1], [30,0,1]],
     [[30,0,-1], [40,0,-1], [0,0,1], [10,0,1], [20,0,1]],
     [[10,0,-1], [0,0,1], [10,0,-1], [0,0,1], [20,0,1]],
     [[0,0,1], [30,0,-1], [20,0,-1], [20,0,-1], [0,0,1]],
]

dfs_a=[[1,1,0,0],[1,1,0,0],[0,1,1,1]]
dfs_b=[[1,1,0,0],[1,1,0,0],[0,0,1,1]]
seq=[1,2,1,4,1,6,3,8,7,10]
seq_b='))((()))()()())(((())'

matrix=[
    [1, 2, 3, 6, 2, 8, 1],
    [4, 8, 2, 4, 3, 1, 9],
    [1, 5, 3, 7, 9, 3, 1],
    [4, 9, 2, 1, 6, 9, 5],
    [7, 6, 8, 4, 7, 2, 6],
    [2, 1, 6, 2, 4, 8, 7],
    [8, 4, 3, 9, 2, 5, 8]]

exp='((7+3)*(((5-2)+2)*3))'
exp_dict={'+':add,'-':sub,'*':mul,'/':truediv}