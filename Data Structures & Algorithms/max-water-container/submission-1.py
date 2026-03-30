class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_hold = 0

        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                total = abs(i -j) * min(heights[i],heights[j])
                if total > max_hold:
                    max_hold = total
        return max_hold