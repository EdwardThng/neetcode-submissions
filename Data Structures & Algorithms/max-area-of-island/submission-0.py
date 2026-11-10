class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = set()
        max_area = 0

        def dfs(r, c):
            if (r < 0 or r >= row or c < 0 or c >= col
                or grid[r][c] != 1 or (r, c) in visited):
                return 0
            area = 1
            visited.add((r, c))
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                area += dfs(r + dr, c + dc)
            return area
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = dfs(r, c)
                    max_area = max(max_area, area)
        return max_area   