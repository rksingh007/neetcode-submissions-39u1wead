class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for x in strs:
            key = "".join(sorted(x))
            if key not in d:
                d[key]=[]
            d[key].append(x)

        
        return (list(d.values()))