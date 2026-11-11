class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for i in range(len(strs)): 
            arr = [0] * 26
            for j in range(len(strs[i])): 
                ind = ord(strs[i][j])-97
                arr[ind]+=1
            key = "" 
            for index in range(26): 
                if arr[index] != 0: 
                    key+=(chr(index+97)*arr[index])
            if key in anagram:
                anagram[key].append(strs[i]) 
            else: 
                anagram[key] = [strs[i]] 
        res = [] 
        for i in anagram: 
            res.append(anagram[i]) 
        return res
        



        