class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R = len(grid)
        C = len(grid[0])

        inf = 2147483647
        q = deque()

        seen = set()

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    q.append([r, c])
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        dist = 0

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (nr < 0 or nr >= R or
                        nc < 0 or nc >= C or
                        grid[nr][nc] != inf):
                        continue
                    
                    grid[nr][nc] = dist + 1
                    q.append([nr, nc])

            dist += 1



        
        