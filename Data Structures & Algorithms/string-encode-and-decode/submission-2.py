class Solution:

    def encode(self, strs: List[str]) -> str:
        s = [] 
        for i in range(len(strs)): 
            s.append(str(len(strs[i])))
            s.append('&')
            for j in range(len(strs[i])): 
                s.append(strs[i][j]) 
        return "".join(s)
                

    def decode(self, s: str) -> List[str]: 
        strs = [] 
        i = 0 
        while i < len(s): 
            chars = ""
            n = int(s[i:].partition('&')[0]) 
            while s[i] != '&': 
                i+=1
            i+=1
            chars = s[i : i+n] 
            strs.append(chars)
            i+=n
        return strs

