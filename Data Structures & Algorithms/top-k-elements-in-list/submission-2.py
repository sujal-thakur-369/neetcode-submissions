class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums)+1)]
        seen = {} 

        for i in range(len(nums)): 
            seen[nums[i]] = seen.get(nums[i],0)+1 
        
        for key,val in seen.items(): 
            bucket[val].append(key)
        ans = []  
        for i in range(len(bucket)-1,0,-1): 
            for j in bucket[i]: 
                ans.append(j) 
            if len(ans) == k: 
                break 
        return ans
            
        