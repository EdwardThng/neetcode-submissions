class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = []
        
        for i in range(len(nums)):
            k = 1
            while k < len(nums):
                if nums[i] + nums[k] == target and i != k:
                    index.append(i)
                    index.append(k)
                    return index 
                else:
                    k += 1
                
        
        return index
            
