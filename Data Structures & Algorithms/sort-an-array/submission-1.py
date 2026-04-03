class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        if len(nums)<=1:
            return nums
        half = len(nums)//2
        left = nums[:half]
        right = nums[half:]

        leftArray = self.sortArray(left)
        rightArray = self.sortArray(right)
        return self.merge(leftArray,rightArray)

    def merge(self,left,right):
        re = []
        i,j=0,0

        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                re.append(left[i])
                i+=1
            else:
                re.append(right[j])
                j+=1

        re.extend(left[i:])
        re.extend(right[j:])
        return re

