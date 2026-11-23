class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {} 
        for i in range(len(nums)): 
            seen[nums[i]] = seen.get(nums[i],0)+1 
        sorted_seen = dict(sorted(seen.items(),key=lambda item: item[1],reverse=True))
        ans = [] 
        for i,(key,value) in enumerate(sorted_seen.items()): 
            if i == k: 
                break 
            ans.append(key)
        return ans
        