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
                    max_value_key = keys
            output.append(max_value_key)
            count += 1
            hashmap.pop(max_value_key)
        
        return output
                
                