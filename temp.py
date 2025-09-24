class Solution:
    def mostProfitablePath(self, edges, bob, amount) :
        adj = defaultdict(list)
        for u, v in edges :
            adj[u].append(v)
            adj[v].append(u)
        
        visited = defaultdict(int)

        def bobdfs(node) :
            visited[node] = amount[node]
            if node == 0 :
                bobpath = visited.copy( )
                return bobpath
            for v in adj[node] :
                if v not in visited :
                    cur =  bobdfs(v)
                    if cur : return cur
            return None
        pathdict = bobdfs(bob)
        bobpath = sum( pathdict.values())
        self.res = float("inf")
        visited = set( )

        def dfs(node , profit) :
            nonlocal bobpath
            
            cur = amount[node]//2 if node in pathdict else amount[node]
            bobpath -= amount[node] // 2 if node in pathdict else amount[node]
            if not adj[node] : 
                self.res = max(self.res, profit + cur)
                return
            visited.add(node)
            for neh in adj[node] :
                if neh not in visited :
                    dfs(neh, profit + cur)
            bobpath += amount[node] // 2 if node in pathdict else amount[node]
            
        dfs(0)
        return self.res