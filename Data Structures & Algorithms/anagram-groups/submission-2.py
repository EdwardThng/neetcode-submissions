class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0 or len(strs) == 1:
            return [strs]

        hashmap = {}
        final = []
        j = 0

        for i in range(len(strs)):
            srted = "".join(sorted(strs[i]))
            if srted in hashmap:
                index = hashmap[srted]
                final[index].append(strs[i])
            else:
                hashmap[srted] = j
                final.append([strs[i]])
                j += 1
        return final