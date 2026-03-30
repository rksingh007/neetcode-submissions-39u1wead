class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=='':
            return 0

        max_len=0
        sub=''
        for char in s:
            if char in sub:
                duplicate_index= sub.index(char)
                sub = sub[duplicate_index+1:]
            sub+=char
            max_len = max(max_len,len(sub))
        return max_len
        