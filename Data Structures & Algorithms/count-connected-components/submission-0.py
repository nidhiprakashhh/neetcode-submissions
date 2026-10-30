class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i : [] for i in range(n)}
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        visit = set()

        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for nei in adj[node]:
                dfs(nei)

        res = 0

        for node in range(n):
            if node not in visit:
                dfs(node)
                res += 1

        return res
        