class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        n=(len(nums))//3
        cnt_num = {}
        # for num in nums:
        #     if num not in result:
        #         if nums.count(num)>n:
        #             result.append(num)
        # return result
        for num in nums:
            cnt_num[num] = cnt_num.get(num,0)+1
        #print(cnt_num)
        for i in cnt_num:
            if cnt_num[i]>n:
                result.append(i)
        return result