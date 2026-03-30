from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # uni_nums = set(nums)
        # if len(uni_nums)==len(nums):
        #     return False
        # else:
        #     return True
        d_n = {}
        for i in nums:
            if i not in d_n:
                d_n[i]=1
            else:
                return True
        return False