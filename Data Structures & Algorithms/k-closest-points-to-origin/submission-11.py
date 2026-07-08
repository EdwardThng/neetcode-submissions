class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k < 0:
            return []
        if k >= len(points):
            return points

        pivot = len(points) - 1
        pivot_distance = points[pivot][0]**2 + points[pivot][1]**2
        left = 0

        for i in range(pivot):
            i_distance = points[i][0]**2 + points[i][1]**2    
            if i_distance < pivot_distance:
                temp = points[left]
                points[left] = points[i]
                points[i] = temp
                left += 1
        
        temp = points[pivot]
        points[pivot] = points[left]
        points[left] = temp

        if left < k:
            return points[:left + 1] + self.kClosest((points[left + 1:]), k - left - 1)
        elif left > k:
            return self.kClosest(points[:left], k)
        else:
            return points[:k]
