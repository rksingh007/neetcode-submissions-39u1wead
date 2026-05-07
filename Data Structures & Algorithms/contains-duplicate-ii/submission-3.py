class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen ={}
        for i,num in enumerate(nums):
            if num in last_seen and i-last_seen[num]<=k:
                return True
            last_seen[num]=i
        return False


        # flag = False
        
        # for i in range(len(nums)):
        #     if len(nums[i:i+k+1])!=len(set(nums[i:i+k+1])):
        #         flag = True
                                    
        # return flag
