class Solution:

    def encode(self, strs: List[str]) -> str:
        re_str = ""
        for word in strs:
            re_str += str(len(word))+"#"+word
        print(re_str)
        return re_str

    def decode(self, s: str) -> List[str]:
        re_lst = []
        i=0
        j=0
        while i<len(s):
            if s[i]=="#":
                n=int(s[j:i])
                i+=1
                re_lst.append(s[i:i+n])
                i=i+n
                j=i

            else:
                i+=1
        print(re_lst)
        return re_lst
