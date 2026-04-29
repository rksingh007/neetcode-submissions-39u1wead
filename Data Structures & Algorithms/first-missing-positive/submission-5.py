class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s= set(nums)
        arr = list(s)
        arr.sort()
        flag = True
        if 1 not in s:
            return 1
        for i in range(1, len(arr)):
            if arr[i]!=arr[i-1]+1 and arr[i-1]+1>0:
                return arr[i-1]+1
                flag = False

                break
        if flag:

            return arr[-1]+1
            