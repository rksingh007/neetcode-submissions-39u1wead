class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l=0
        max_fr = 0
        max_len =0
        # for i in range(len(s)):
        #     count[s[i]] = count.get(s[i],0)+1
        #     max_fr = max(max_fr,count[s[i]])
        #     if (i-l+1) -max_fr > k:
        #         count[s[l]]-=1
        #         l+=1
        #     max_len = max(max_len,i-l+1)
        # return max_len
        for i in range(len(s)):
            count[s[i]] = count.get(s[i],0)+1

            max_fr = max(max_fr, count[s[i]])

            if (i-l +1)-max_fr >k:
                count[s[l]]-=1
                l+=1
            max_len = max(max_len,i-l+1)
        print(max_len)
        return max_len

