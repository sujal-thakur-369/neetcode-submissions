class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        curr = 0
        for i in range(len(strs[0])): 
            seen = {}
            for j in range(len(strs)):
                seen[strs[j][i]] = seen.get(strs[j][i],0)+1
            if len(seen) > 1: 
                return "".join(res)
            char,_ = seen.popitem() 
            res.append(char) 
        return "".join(res)
                 

        