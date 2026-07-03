class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = []
        k = 0
        i = 1

        while i < len(nums):
            if nums[k] + nums[i] == target:
                index.append(k)
                index.append(i)
                return index
            else:
                i += 1
            
            
