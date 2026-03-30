class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_hold = 0
        l = 0
        r = len(heights)-1
        while l < r:
            area = min(heights[l],heights[r]) * abs((r-l))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            if area>max_hold:
                max_hold = area
        return (max_hold)