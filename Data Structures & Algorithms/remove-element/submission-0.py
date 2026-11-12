class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0 or (len(nums) == 1 and nums[0] == val): 
            return 0
        left,right = 0,len(nums)-1

        while left <= right:
            while right >= left and nums[right] == val:
                right-=1
            if nums[left] == val and left <= right:
                nums[left],nums[right]=nums[right],nums[left]
                right-=1
            left+=1
        
        return left
        