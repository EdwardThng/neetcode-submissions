class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        srted = sorted(nums)
        final = []

        for i in range(len(srted) - 2):
            j = i + 1
            k = len(srted) - 1
            difference = -srted[i]
            if i > 0 and srted[i] == srted[i - 1]:
                continue
            while j < k:
                if srted[j] + srted[k] > difference:
                    k -= 1
                elif srted[j] + srted[k] < difference:
                    j += 1
                else:
                    final.append([srted[i], srted[k], srted[j]
                    ])
                    j += 1
                    k -= 1
                    
                    while j < k and srted[j] == srted[j - 1]:
                        j += 1
                    while j < k and srted[k] == srted[k + 1]:
                        k -= 1
        return final   