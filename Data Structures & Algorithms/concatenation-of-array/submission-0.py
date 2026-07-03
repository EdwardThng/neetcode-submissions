class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new = []
        for i in range(len(nums)):
            new.append(nums[i])
        return nums + new