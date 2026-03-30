from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''s=sorted(s)
        t =sorted(t)
        return s==t'''
        if len(s)>len(t):
            s1=s
        else:
            s1=t
        
        for i in s1:
            if s.count(i)!=t.count(i):
                return False
        return True
        

