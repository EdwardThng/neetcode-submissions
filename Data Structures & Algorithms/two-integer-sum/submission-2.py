class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = []
        k = 1
        
        for i in range(len(nums)):
            while k < len(nums):
                if nums[i] + nums[k] == target:
                    index.append(i)
                    index.append(k)
                    return index 
                else:
                    k += 1
        
        return index
            
