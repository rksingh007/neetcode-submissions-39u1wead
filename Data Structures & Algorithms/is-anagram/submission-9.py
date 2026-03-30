from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t) or set(s) != set(t):
            return False
        d_s,d_t=Counter(s),Counter(t)
        return d_s==d_t