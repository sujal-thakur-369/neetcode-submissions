class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        seen = [0] * 26 
        for i in range(len(s)): 
            index = ord(s[i]) - 97 
            seen[index]+=1 
        
        for i in range(len(t)): 
            index = ord(t[i]) - 97 
            seen[index]-=1 
        
        for i in seen: 
            if i != 0: 
                return False 
        return True





        