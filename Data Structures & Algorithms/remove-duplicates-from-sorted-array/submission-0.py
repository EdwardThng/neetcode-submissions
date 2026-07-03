class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new = []
        for i in range(len(nums)):
            if nums[i] not in new:
                new.append(nums[i])
        
        return len(new)