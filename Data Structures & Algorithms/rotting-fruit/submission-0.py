class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        time = 0
        freshFruit = 0

        q = deque()

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    freshFruit += 1
                elif grid[r][c] == 2:
                    q.append([r, c])

        directions = [[0, 1],[1, 0], [0, -1], [-1, 0]]
        while q and freshFruit > 0:
            qLen = len(q)
            for i in range(qLen):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (nr < 0 or nr >= R or
                        nc < 0 or nc >= C):
                        continue
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        freshFruit -= 1
                        q.append([nr, nc])
            time += 1

        if freshFruit == 0:
            return time
        else:
            return -1

                     