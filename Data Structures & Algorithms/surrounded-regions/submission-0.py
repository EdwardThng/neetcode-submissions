from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        circles = []

        for c in range(cols):
            if board[0][c] == "O":
                circles.append((0, c))
        for r in range(1, rows):
            if board[r][-1] == "O":
                circles.append((r, cols - 1))
        for c in range(cols - 1):
            if board[rows - 1][c] == "O":
                circles.append((rows - 1, c))
        for r in range(1, rows - 1):
            if board[r][0] == "O":
                circles.append((r, 0))
        
        def bfs(start):
            visited = set(start)
            d = deque(start)
            
            while d:
                r, c = d.popleft()
                for dr, dc in ([1, 0], [0, 1], [-1, 0], [0, -1]):
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols 
                    and board[nr][nc] == "O" and (nr, nc) not in visited):
                        visited.add((nr, nc))
                        d.append((nr, nc))
    
            return visited
        
        crcl = bfs(circles)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in crcl:
                    board[r][c] = "X"
        