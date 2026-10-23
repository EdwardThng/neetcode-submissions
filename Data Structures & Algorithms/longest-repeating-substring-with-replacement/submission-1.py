class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        l = 0
        max_length = 0

        for r in range(len(s)):
            if s[r] not in hashmap:
                hashmap[s[r]] = 1
            else:
                hashmap[s[r]] += 1
            
            max_freq = max(hashmap.values())
            window_size = r - l + 1
            if window_size - max_freq > k:
                hashmap[s[l]] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)
        return max_length