from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k <= 0 or not points:          # base cases (bug 2)
            return []
        if k >= len(points):
            return points
        
        pivot = len(points) - 1
        left = 0
        result = []

        for i in range(len(points)):
            pivot_distance = (sqrt((0 - points[pivot][0])**2 + (0 - points[pivot][1])**2))
            i_distance = (sqrt((0 - points[i][0])**2 + (0 - points[i][1])**2))

            if i_distance < pivot_distance:
                temp = points[i]
                points[i] = points[left]
                points[left] = temp
                left += 1
        temp = points[pivot]
        points[pivot] = points[left]
        points[left] = temp

        if left < k:
            return points[:left + 1] + self.kClosest(points[left + 1:], k - left - 1)
        elif left > k:
            return self.kClosest(points[:left], k)
        else:
            j = 0
            while j < k:
                result.append(points[j])
                j += 1
            return result
                
        


        
        
                