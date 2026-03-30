from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t) and set(s) == set(t):
            d_s = Counter(s)
            d_t = Counter(t)
            for i in d_s:
                if d_s[i]==d_t[i]:
                    return True

        return False



