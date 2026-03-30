from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result =''
        countT = Counter(t)
        n=len(s)
        min_len = float('inf')

        for i in range(n):
            countS={}
            for j in range(i,n):
                countS[s[j]]=countS.get(s[j],0)+1

                valid = True
                for k in countT:
                    if countS.get(k,0)<countT[k]:
                        valid = False
                        break
                if valid:
                    if (j-i+1)<min_len:
                        min_len=j-i+1
                        result= s[i:j+1]

        return result

