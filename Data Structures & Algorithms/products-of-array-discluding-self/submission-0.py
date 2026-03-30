class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i=0
        re_lst=[]
        while i<len(nums):
            j=0
            prod = 1
            while j<len(nums):
                if j==i:
                    j+=1
                    continue
                else:
                    prod*=nums[j]
                    j+=1
            re_lst.append(prod)
            i+=1
            prod=1
        return re_lst


