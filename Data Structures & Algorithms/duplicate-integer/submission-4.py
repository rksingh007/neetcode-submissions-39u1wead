from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uni_nums = set(nums)
        if len(uni_nums)==len(nums):
            return False
        else:
            return True