import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        heap = []

        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else:
                hashmap[nums[i]] += 1
        for key in hashmap:
            heapq.heappush(heap, (hashmap[key], key))
        while len(heap) > k:
            heapq.heappop(heap)
        return [key for freq, key in heap]