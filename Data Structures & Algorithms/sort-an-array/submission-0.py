import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heap = []
        final = []

        for i in range(len(nums)):
            heapq.heappush(heap, nums[i])
        for j in range(len(heap)):
            final.append(heapq.heappop(heap))
        
        return final