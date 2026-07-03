class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        j = 0
        hashset = set()
        maximum = 0

        for i in range(len(s)):
            while s[i] in hashset:
                hashset.remove(s[j])
                j += 1
            hashset.add(s[i])
            maximum = max(maximum, i - j + 1)

        return maximum    