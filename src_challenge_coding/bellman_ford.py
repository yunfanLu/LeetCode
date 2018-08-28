

class edge:
    def __init__(self, _from, _to, _cost):
        """
        一条边有三个属性，从哪来，到哪儿，权重多少。
        """
        self.fromp = _from
        self.to = _to
        self.cost = _cost

# 权重小于 INF，权重为 INF 表明两点之间没有边相连
INF = 123456789
# 最多有多少点，对于有向图最多有(V*(V-1))条边
MAX_V = 1000
MAX_E = MAX_V * (MAX_V - 1)
es = [
    edge(0,1,1),
    edge(1,0,1),
    edge(1,2,1),
    edge(2,1,1),
    edge(0,3,1),
    edge(3,0,1),
    edge(3,2,4),
    edge(2,3,4),
]

d = [INF for i in range(MAX_V)]
V, E = 100, 100*100

def shortest_path(s):
    for i in range(len(d)):
        d[i] = INF
    d[s] = 0
    while(True):
        update = False
        for e in es:
            if d[e.fromp] != INF and d[e.to] > d[e.fromp] + e.cost:
                d[e.to] = d[e.fromp] + e.cost
                update = True
        if update is False:
            break

def find_negative_loop():
    for i in range(len(d)):
        d[i] = 0
    for i in range(V):
        for e in es:
            if d[e.to] > d[e.fromp] + e.cost:
                d[e.to] = d[e.fromp] + e.cost
            if i == V - 1:
                return True
    return False