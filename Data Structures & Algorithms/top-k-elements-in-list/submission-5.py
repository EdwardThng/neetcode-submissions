import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else:
                hashmap[nums[i]] += 1
        
        min_queue = []
        for key in hashmap:
            heapq.heappush(min_queue, (hashmap[key], key))
            if len(min_queue) > k:
                heapq.heappop(min_queue)
        result = [j[1] for j in min_queue]
        return result