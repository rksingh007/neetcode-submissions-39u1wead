class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        re_l =[]
        for i in range(len(nums)-k+1):
            l= set(nums[i:i+k])
            re_l.append(max(l))


        return re_l