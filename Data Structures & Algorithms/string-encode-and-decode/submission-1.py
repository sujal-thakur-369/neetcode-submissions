class Solution:

    def encode(self, strs: List[str]) -> str:
        s = [] 
        for i in range(len(strs)): 
            s.append(str(len(strs[i])))
            for j in range(len(strs[i])): 
                s.append(strs[i][j]) 
        return "".join(s)
                

    def decode(self, s: str) -> List[str]: 
        strs = [] 
        i = 0 
        while i < len(s): 
            chars = ""
            n = int(s[i]) 
            chars = s[i+1 : i+n+1] 
            strs.append(chars)
            i+=n+1
        return strs

