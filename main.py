from collections import deque

def bfs_chess_knight(x,y):
    letters='abcdefgh'
    numbers='12345678'
    g={i+j:set() for i in letters for j in numbers}

    def add_g(v1,v2):
        g[v1].add(v2)
        g[v2].add(v1)

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

    distances={i:None for i in g}
    parents=distances.copy()

    distances[x]=0
    q=deque()
    q.append(x)

    while q:
        v=q.popleft()
        for i in g[v]:
            if distances[i] is None:
                distances[i]=distances[v]+1
                parents[i]=v
                q.append(i)
    path=[y]
    parrent=parents[y]
    while not parrent is None:
        path.append(parrent)
        parrent=parents[parrent]
    return path[::-1]


print(bfs_chess_knight('d4','f7'))