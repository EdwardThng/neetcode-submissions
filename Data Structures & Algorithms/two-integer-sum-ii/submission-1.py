class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff not in hashmap:
                hashmap[numbers[i]] = 0
                hashmap[numbers[i]] += i
            elif hashmap[diff] < i:
                return [hashmap[diff] + 1, i + 1]
            else:
                return [i + 1, hashmap[diff] + 1]