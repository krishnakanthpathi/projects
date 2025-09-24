class UnionFind :
    def __init__(self , n ) :
        self.parent = [-1 for _ in range(n) ]
        self.rank = [0 for _ in range(n) ]

    def union(self , n1 , n2) :
        par1 = self.find(n1)
        par2 = self.find(n2)

        if par1 == par2 :
            return False

        if self.rank[par1] > self.rank[par2] :
            self.parent[par2] = par1
            self.rank[par1] += self.rank[par2]
        elif self.rank[par2] > self.rank[par1] :
            self.parent[par1] = par2
            self.rank[par2] += self.rank[par1]
        else:
            self.parent[par2] = par1
            self.rank[par1] += 1
        return True

    def find(self , node) :
        if self.parent[node] == -1 :
            return node
        par = self.find(self.parent[node])
        self.parent[node] = par
        return par