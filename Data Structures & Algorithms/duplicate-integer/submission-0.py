class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i = 0
        copy = []

        for i in range(len(nums)):
            copy.append(nums[i])
            if nums[i] in copy:
                return True 
                
        return False
