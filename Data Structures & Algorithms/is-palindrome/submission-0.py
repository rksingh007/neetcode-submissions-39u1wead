import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join(s.split())
        s=s.lower()
        translator = str.maketrans('', '', string.punctuation)
        s=s.translate(translator)

        j=len(s)-1
        for i in range(len(s)):
            if s[i]==s[j]:
                j-=1
            elif i==j:
                break
            else:
                return False
        return True
