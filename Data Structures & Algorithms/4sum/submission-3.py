class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        re =set(())
        for i in range(n):
            for j in range(i+1,n):
                for f in range(j+1,n):
                    for l in range(f+1,n):
                        if nums[i]+nums[j]+nums[f]+nums[l] == target:        
                            re.add((nums[i],nums[j],nums[f],nums[l]))
        return list(re)