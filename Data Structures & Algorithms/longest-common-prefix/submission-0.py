class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prifix = strs[0]
        for word in strs:
            while prifix != word[:len(prifix)]:
                prifix = prifix[:-1]

            if prifix == "":
                return ""
        return prifix


            