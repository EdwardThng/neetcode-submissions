from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(numCourses)]
        indeg = [0] * numCourses

        for a, b in prerequisites:
            adj[b].append(a)
            indeg[a] += 1
        
        queue = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                queue.append(i)
        
        taken = 0
        while queue:
            node = queue.popleft()
            taken += 1
            for j in adj[node]:
                indeg[j] -= 1
                if indeg[j] == 0:
                    queue.append(j)
        
        if taken == numCourses:
            return True
        
        return False