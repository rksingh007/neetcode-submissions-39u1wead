class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt ={}
        fre_ele=[]
        for num in nums:
            if num not in cnt:
                cnt[num]=1
            else:
                cnt[num]+=1
        for i in range(k):
            fre_ele.append(max(cnt,key=cnt.get))
            del(cnt[max(cnt,key=cnt.get)])

        print(fre_ele)
        return fre_ele