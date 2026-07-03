class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        copy = []
        i = 0

        while i < len(nums) and nums[i] not in copy:
            copy.append(nums[i])
            i += 1
        
        if i < len(nums):
            return True 
        
        return False
