class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        n=(len(nums))//3
        for num in nums:
            if num not in result:
                if nums.count(num)>n:
                    result.append(num)
        return result