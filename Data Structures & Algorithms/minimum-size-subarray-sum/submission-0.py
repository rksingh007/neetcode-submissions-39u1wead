class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        re = float("inf")
        left= 0
        curr_sum = 0
        for right in range(len(nums)):
            curr_sum+=nums[right]
            while curr_sum>=target:
                re=min(re,right-left+1)
                curr_sum-=nums[left]
                left+=1
        if re == float("inf"):
            return 0
        return re