class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff not in hashmap:
                hashmap[numbers[i]] = 0
                hashmap[numbers[i]] += 1
            if diff < numbers[i]:
                return [diff, numbers[i]]
            else:
                return [numbers[i], diff]