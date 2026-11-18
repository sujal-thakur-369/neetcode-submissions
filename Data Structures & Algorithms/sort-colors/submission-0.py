class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0 
        high = len(nums)-1 
        for i in range(len(nums)): 
            while nums[high] == 2: 
                high -=1 
            while nums[low] == 0: 
                low+=1 
            if i > high: 
                break
            if nums[i] == 2 and i < high: 
                nums[i],nums[high] = nums[high],nums[i] 
                high-=1 
            if nums[i] == 0 and i > low: 
                nums[i],nums[low] = nums[low],nums[i] 
                low+=1 
