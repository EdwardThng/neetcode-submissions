class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference not in hashmap:
                hashmap[nums[i]] = i
            else:
                return [hashmap[difference], i]