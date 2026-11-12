class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0: 
            return 0
        left,right = 0,len(nums)-1

        while left <= right:
            while right >= left and nums[right] == val:
                right-=1
            if nums[left] == val and left <= right:
                nums[left],nums[right]=nums[right],nums[left]
                right-=1
            left+=1
        
        return left if right >= 0 else 0
        