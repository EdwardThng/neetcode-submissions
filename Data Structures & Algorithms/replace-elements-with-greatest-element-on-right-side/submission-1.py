class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = len(arr) - 2
        max = arr[-1]
        
        while i >= 0:
            if arr[i] > max:
                temp = arr[i]
                arr[i] = max
                max = temp
            else:
                arr[i] = max
            i -= 1
        
        arr[-1] = -1

        return arr
