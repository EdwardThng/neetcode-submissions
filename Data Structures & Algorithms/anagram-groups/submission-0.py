class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        output = []
        for i in range(len(strs)):
            sortedString = str(sorted(strs[i]))
            if sortedString not in hashmap:
                hashmap[sortedString] = []
                hashmap[sortedString].append(strs[i])
            else:
                hashmap[sortedString].append(strs[i])
        
        output = []
        for keys in hashmap:
            output.append(hashmap[keys])
        
        return output 
        
       
        
            
