class Solution:

    def encode(self, strs: List[str]) -> str:
        s = "" 
        for i in range(len(strs)): 
            for j in range(len(strs[i])): 
                s+=strs[i][j] 
            s+="\n" 
        return s
                

    def decode(self, s: str) -> List[str]: 
        strs = [] 
        chars = "" 
        for i in range(len(s)):
            if s[i] == "\n": 
                strs.append(chars) 
                chars = "" 
                continue 
            chars+=s[i] 
        return strs

