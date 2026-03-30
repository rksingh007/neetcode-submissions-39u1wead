class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        total_water =0
        for i in range(n):
            left_max = 0
            for j in range(i):
                left_max=max(left_max, height[j])
            right_max = 0
            for j in range(i+1,n):
                right_max = max(right_max,height[j])
            water = min(left_max,right_max) - height[i]
            if water >0:
                total_water+=water
        return total_water
                                                    