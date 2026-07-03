class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        output = []
        count = 0

        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 0
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] += 1
        
        while count < k:
            max_value = 0
            for keys in hashmap:
                if hashmap[keys] > max_value:
                    max_value = hashmap[keys]
            output.append(keys)
            count += 1
            hashmap.pop(keys)
        
        return output
                
                