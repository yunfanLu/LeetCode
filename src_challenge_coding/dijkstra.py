
INF = 123456789

def dijkstra(s, cost, V):
    """
    s: int source point
    coysr: List[List[int]]
    V: int point count
    """
    d = [INF for i in range(V)]
    used = [False for i in range(V)]
    d[s] = 0

    while True:
        v = -1
        for u in range(V):
            if (used[u] is False) and (v == -1 or d[u] < d[v]):
                v = u
        if v == -1:
            break
        used[v] = True
        for i in range(V):
            d[i] = min(d[i], d[v] + cost[v][i])
    return d

cost = [
    [0, 1, INF, 1],
    [1, 0, 1, INF],
    [INF, 1, 0, 4],
    [1, INF, 4, 0]
]
print(dijkstra(0, cost, 4))