class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums_set = set(nums)
        lst = list(nums_set)
        max_counter = 0

        for i in nums_set:
            if i - 1 not in nums_set:
                current = i
                counter = 1
                while current + 1 in nums_set:
                    current += 1
                    counter += 1
                if counter > max_counter:
                    max_counter = counter
        return max_counter