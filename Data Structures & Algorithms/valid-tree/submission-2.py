class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        adj = {i: [] for i in range(n)}
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        visit = set()
        def dfs(node, prev):
            if node in visit:
                return False
                
            visit.add(node)
            for nei in adj[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        return dfs(0, -1) and n == len(visit)
        