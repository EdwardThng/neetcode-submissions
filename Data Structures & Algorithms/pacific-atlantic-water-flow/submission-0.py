from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac = []
        atl = []

        for c in range(cols):
            pac.append((0, c))
        for r in range(1, rows):
            pac.append((r, 0))

        for c in range(cols):
            atl.append((rows - 1, c))
        for r in range(rows - 1):
            atl.append((r, cols - 1))

        def bfs(starts):
            visited = set(starts)
            d = deque(starts)
            while d:
                r, c = d.popleft()
                for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols and
                    heights[nr][nc] >= heights[r][c] and 
                    (nr, nc) not in visited):
                        visited.add((nr, nc))
                        d.append((nr, nc))
            return visited
        
        pacific = bfs(pac)
        atlantic = bfs(atl)

        return [[r, c] for (r, c) in pacific & atlantic]



