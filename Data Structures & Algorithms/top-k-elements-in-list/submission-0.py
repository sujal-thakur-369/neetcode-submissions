class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {} 
        for i in range(len(nums)): 
            seen[nums[i]] = seen.get(nums[i],0)+1 
        ans = [] 
        for i,(key,value) in enumerate(seen.items()): 
            if value >= k: 
                ans.append(key) 
        return ans
        