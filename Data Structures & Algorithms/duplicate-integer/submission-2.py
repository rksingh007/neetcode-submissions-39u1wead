from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''set_nums = set(nums)
        if len(set_nums)==len(nums):
            return False
        else:
            return True'''
        if nums:
            d = Counter(nums)
            if max(d.values())>1:
                return True
        return False
            
        