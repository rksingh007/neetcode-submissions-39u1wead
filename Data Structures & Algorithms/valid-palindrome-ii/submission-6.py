class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r,c = 0,len(s)-1,1

        while l<=r+1:
            if l>=r:
                return True
                
            if s[l]==s[r]:
                l+=1
                r-=1
                
            elif s[l]!=s[r]:
                if s[l+1]==s[r]:
                    c-=1
                    r-=1
                elif s[r-1]==s[l]:
                    c-=1
                    l+=1
                    
                elif c==-1:
                    return False
                    
                else:
                    return False
