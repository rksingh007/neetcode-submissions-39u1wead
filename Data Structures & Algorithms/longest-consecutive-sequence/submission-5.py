class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''nums=sorted(list(set(nums)))

        if nums:
            pre_val = nums[0]
            length = 1
            re_l=[]
            
            for i in range(0,len(nums)):
                if nums[i]==pre_val+1:
                    pre_val = nums[i]
                    length+=1
                elif nums[i]==pre_val-1:
                    continue
                else:
                    re_l.append(length)
                    length = 1
                    pr_val = nums[i]
            re_l.append(length)
            print(re_l)
            return max(re_l)
        return 0'''
        if nums:
            nums=sorted(list(set(nums)))
            pr_val = nums[0] # -1,0,1
            length = 1
            re_l = []
            for i in range(0,len(nums)):
                if nums[i]==pr_val+1: # -1=0, 0=0,1=1,3=2,4=1
                    length+=1         # 2,3
                    pr_val = nums[i]
                    print(length)
                elif nums[i]==pr_val-1:
                    continue
                else:
                    re_l.append(length)
                    length = 1
                    pr_val = nums[i]
            re_l.append(length)
            print(re_l)
            return max(re_l)
        return 0

    
