class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for i in range(len(nums))]
         
        for i in range(1,len(nums)):
            res[i] = nums[i-1] * res[i-1]
        
        r = 1 
        for i in range(len(nums)-1, -1, -1):
            res[i] *= r  
            r *= nums[i]
        
        return res
