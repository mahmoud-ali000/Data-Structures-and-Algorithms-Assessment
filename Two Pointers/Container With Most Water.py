from typing import List


# the area = min(left, right) * width
# [1,8,6,2,5,4,8,3,9,7]
# (0,1), (1,8) -> 1*1=1
# (2,6) 1to6=2*1 or 8to6=1*6

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, 1
        container = 0
        while True:
            container = max(
                container,
                min(height[l], height[r]) * r-l
            )
            r += 1
            

                
