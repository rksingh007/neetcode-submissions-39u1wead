class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        flag = False
        
        for i in range(len(nums)):
            if len(nums[i:i+k+1])!=len(set(nums[i:i+k+1])):
                flag = True
                                    
        return flag
