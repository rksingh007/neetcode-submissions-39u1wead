class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r,c = 0,len(s)-1,1

        while l<=r+1:
            if l>=r:
                return True
                break
            if s[l]==s[r]:
                l+=1
                r-=1
            elif s[l]!=s[r]:
                if s[l+1]==s[r]:
                    s.replace(s[l],"")
                    c-=1
                    r-=1
                elif s[r-1]==s[l]:
                    s.replace(s[r],"")
                    c-=1
                    l+=1
                elif c==-1:
                    return False
                    break
                else:
                    return False
                    break
