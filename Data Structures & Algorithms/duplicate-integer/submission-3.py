class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}

        for i in nums:
            hashmap[i] = 0
        for j in nums:
            hashmap[j] += 1
            if hashmap[j] > 1:
                return True 
        
        return False
    

