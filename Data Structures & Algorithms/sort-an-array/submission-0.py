class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr1,arr2): 
            n = len(arr1)
            m = len(arr2)
            merged_arr = []
            i,j = 0,0 
            while i<n and j<m: 
                if arr1[i] <= arr2[j]: 
                    merged_arr.append(arr1[i]) 
                    i+=1 
                else: 
                    merged_arr.append(arr2[j]) 
                    j+=1
            while i<n or j<m: 
                if i<n: 
                    merged_arr.append(arr1[i]) 
                    i+=1 
                else:  
                    merged_arr.append(arr2[j]) 
                    j+=1 
            print(merged_arr)
            return merged_arr 
        def merge_sort(arr,i,n): 
            if n-i == 1: 
                return [arr[i]] 
            else: 
                arr1 = merge_sort(arr,i,(i+n)//2)
                arr2 = merge_sort(arr,(i+n)//2,n) 
                return merge(arr1,arr2) 
        return merge_sort(nums,0,len(nums))

        