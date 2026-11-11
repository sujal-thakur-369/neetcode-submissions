class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for i in range(len(strs)): 
            curr_sum = 0
            for j in range(len(strs[i])): 
                curr_sum+=ord(strs[i][j])
            if curr_sum in anagram:
                anagram[curr_sum].append(strs[i]) 
            else: 
                anagram[curr_sum] = [strs[i]] 
        res = [] 
        for i in anagram: 
            res.append(anagram[i]) 
        return res
        



        