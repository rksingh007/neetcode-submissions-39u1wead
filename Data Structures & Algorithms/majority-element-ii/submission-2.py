class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        n=len(nums)//3
        count1=count2=0
        candidate1 = candidate2 = None
        for num in nums:
            if candidate1==num:
                count1+=1
            elif candidate2==num:
                count2+=1
            elif count1==0:
                candidate1 = num
                count1 =1
            elif count2==0:
                candidate2=num
                count2=1
            else:
                count1-=1
                count2-=1
        
        for c in [candidate1, candidate2]:
            if c is not None and nums.count(c)>n:
                result.append(c)
        return result
        # cnt_num = {}
        # # for num in nums:
        # #     if num not in result:
        # #         if nums.count(num)>n:
        # #             result.append(num)
        # # return result
        # for num in nums:
        #     cnt_num[num] = cnt_num.get(num,0)+1
        # #print(cnt_num)
        # for i in cnt_num:
        #     if cnt_num[i]>n:
        #         result.append(i)
        # return result