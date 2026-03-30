class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)//2

        coutNum = {}
        for i in range(len(nums)):
            coutNum[nums[i]] = (coutNum.get(nums[i], 0) +1)

        for i in nums:
            if coutNum.get(i, 0) > n:
               return i
        