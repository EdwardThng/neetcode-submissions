from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        d = deque([])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    d.append((r, c))
        
        while d:
            r, c = d.popleft()
            for dr, dc in ([1, 0], [0, 1], [-1, 0], [0, -1]):
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols
                and grid[nr][nc] == 2147483647):
                    grid[nr][nc] = grid[r][c] + 1
                    d.append((nr, nc))
        