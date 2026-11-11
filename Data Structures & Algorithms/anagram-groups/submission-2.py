class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for i in range(len(strs)): 
            arr = [0] * 26
            for j in range(len(strs[i])): 
                ind = ord(strs[i][j])-97
                arr[ind]+=1
            if tuple(arr) in anagram:
                anagram[tuple(arr)].append(strs[i]) 
            else: 
                anagram[tuple(arr)] = [strs[i]] 
        res = [] 
        for i in anagram: 
            res.append(anagram[i]) 
        return res
        



        