class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        seen = {")" : "(", "]": "[", "}": "{", ">": "<"}
        for ch in s:
            if ch in seen:
                if not stack or seen[ch] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return len(stack)==0