from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        deg = [0] * numCourses
        queue = deque([])
        final = []

        for a, b in prerequisites:
            adj[b].append(a)
            deg[a] += 1

        for i in range(len(deg)):
            if deg[i] == 0:
                queue.append(i)
        
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                for j in adj[node]:
                    deg[j] -= 1
                    if deg[j] == 0:
                        queue.append(j)
                final.append(node)
        
        if len(final) == numCourses:
            return final
        else:
            return []