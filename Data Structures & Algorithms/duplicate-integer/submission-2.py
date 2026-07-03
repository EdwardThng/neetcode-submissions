class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for i in range(len(nums)):
            if nums[i] not in hashset:
                hashset.add(nums[i])
            elif nums[i] in hashset:
                return True
        
        return False
        