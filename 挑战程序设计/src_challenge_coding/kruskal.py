
class edge:
    def __init__(self, u, v, cost):
        self.u = u
        self.v = v
        self.cost = cost
    
    def __lt__(self, o):
        return self.cost < o.cost

class UnionFindSet:
    def __init__(self, N):
        self.par = [i for i in range(N)]
        self.rank = [0 for i in range(N)]

    def find(self, x):
        if x == self.par[x]:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            self.par[y] = x
        elif self.rank[x] < self.rank[y]:
            self.par[y] = x
        else:
            self.par[x] = y
            self.rank[y] += 1
    
    def same(self, x, y):
        return self.find(x) == self.find(y)



def kruskal(edges, V, E):
    Es = sorted(edges)
    unset = UnionFindSet(V)

    res = 0
    for e in Es:
        if unset.same(e.u, e.v) is False:
            res += e.cost
            unset.union(e.u, e.v)
    return res

INF = 123456789
edges = [
    edge(0,1,1),
    edge(1,0,1),
    edge(1,2,1),
    edge(2,1,1),
    edge(0,3,1),
    edge(3,0,1),
    edge(2,3,1),
    edge(3,2,1),
]
print(kruskal(edges, 4, len(edges)))