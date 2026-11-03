import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-n for n in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x = -heapq.heappop(maxHeap)
            y = -heapq.heappop(maxHeap)

            if x == y:
                continue
            elif y < x: 
                heapq.heappush(maxHeap, y - x)
        if len(maxHeap) == 0:
            return 0
        else:
            return -maxHeap[0]
