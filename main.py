from collections import deque
from gen_graph import generate_chess_grafh,convert_two_dimensional_array_to_graph


def bfs(x,y):
    g=generate_chess_grafh()

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


print(convert_two_dimensional_array_to_graph([[1,2],[2,3],[3,4],[1,4],[1,5]]))
print(convert_two_dimensional_array_to_graph([[9,10],[5,8],[2,6],[1,5],[3,8],[4,9],[8,10],[4,10],[ 6,8],[7,9]]))