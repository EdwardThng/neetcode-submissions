class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) > h:
            return -1

        low = 1
        high = max(piles)
        ans = 0

        while low <= high:
            mid = ((low + high) // 2)
            hours = 0
            for i in range(len(piles)):
                if mid >= piles[i]:
                    hours += 1
                else:
                    hours += math.ceil(piles[i] / mid)

            if hours > h:
                low = mid + 1
            elif hours <= h:
                ans = mid
                high = mid - 1
                
        return ans
