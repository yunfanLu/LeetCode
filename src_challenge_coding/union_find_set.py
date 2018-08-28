class UnionFindSet:
    def __init__(self, N):
        self.par = [i for i in range(N)]
        self.rank = [0 for i in range(N)]

    def find(self, x):
        if x ==  self.par[x]:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return

        if self.rank[x] == self.rank[y]:
            self.par[y] = x
            self.rank[x] += 1
        elif self.rank[x] > self.rank[y]:
            self.par[y] = x
        else:
            self.rank[x] = y
    
    def same(self, x, y):
        return self.find(x) == self.find(y)

unset = UnionFindSet(8)
unset.union(1,2)
unset.union(2,6)
unset.union(3,4)
unset.union(4,5)
unset.union(5,7)

print(unset.same(1,2))
print(unset.same(1,4))
print(unset.same(3,7))