import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        if len(points) == 0:
            return final

        for i in range(len(points)):
            distance = math.sqrt((points[i][0])**2 + (points[i][1]**2))
            heapq.heappush(heap, (-distance, points[i]))

        while len(heap) > k:
            heapq.heappop(heap)

        return [point for distance, point in heap]