class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
    
        count_s1 =[0]*26
        count_s2 = [0]*26
        n1 = len(s1)
        n2 = len(s2)
        if n1>n2:
            return False

        for i in range(n1):

            count_s1[ord(s1[i]) - ord('a')] +=1
            count_s2[ord(s2[i]) - ord('a')] +=1
            print(count_s1,count_s2)

        if count_s1==count_s2:
            return True
        for j in range(n2-n1):
            count_s2[ord(s2[n1+j]) - ord('a')] +=1
            count_s2[ord(s2[j]) - ord('a')] -=1
            if count_s1==count_s2:
                return True

        return False



