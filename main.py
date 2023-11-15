from collections import deque
from gen_graph import generate_chess_bishop_graph


def bst(x,y):
    g=generate_chess_bishop_graph()
    distances={i:None for i in g}
    parents=distances.copy()
    distances[x]=0
    q=deque([x])

    while q:
        v=q.popleft()
        for i in g[v]:
            if distances[i] is None:
                distances[i]=distances[v]+1
                parents[i]=v
                q.append(i)
    
    path=[y]
    parent=parents[y]

    while not parent is None:
        path.append(parent)
        parent=parents[parent]

    return path[::-1]


print(bst('a1','e3'))