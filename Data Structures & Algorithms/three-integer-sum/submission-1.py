class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=[]
        for i in range(len(nums)):
            seen = set()
            for j in range(i+1,len(nums)):
                target = -(nums[i] + nums[j])
                if target in seen:
                    triplet = sorted([nums[j],nums[i],target])
                    if triplet not in l:
                        l.append(triplet)
                seen.add(nums[j])
        return l