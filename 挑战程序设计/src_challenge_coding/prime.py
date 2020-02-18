INF = 123456789

def prime(cost, V):
    """
    cost: List[List[int]]
    v: int
    """
    mincost = [INF for i in range(V)]
    used = [False for i in range(V)]
    
    mincost[0] = 0
    res = 0

    while True:
        v = -1
        for u in range(V):
            if used[u] is False and (v == -1 or mincost[u] < mincost[v]):
                v = u

        if v == -1:
            break
        used[v] = True
        res += mincost[v]

        for u in range(V):
            mincost[u] = min(mincost[u], cost[v][u])
            #  dijkstra: d[i] = min(d[i], d[v] + cost[v][i])
    return res

import pudb
pudb.set_trace()

cost = [
    [0, 1, INF, 1],
    [1, 0, 1, INF],
    [INF, 1, 0, 4],
    [1, INF, 4, 0]
]
print(prime(cost, 4))