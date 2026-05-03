class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        re =[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for f in range(j+1,len(nums)):
                    for l in range(f+1,len(nums)):
                        if nums[i]+nums[j]+nums[f]+nums[l] == target and sorted([nums[i],nums[j],nums[f],nums[l]]) not in re:        
                            re.append(sorted([nums[i],nums[j],nums[f],nums[l]]))
        return re