class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2  = len(s2)
        s1= sorted(s1)
        if n1>n2:
            return False
        for i in range(n2-n1+1):
            sub = s2[i:i+n1]
            if s1==sorted(sub):
                return True
        return False