"""
#Explanation

Sort input A first,
For each A[i], find out the maximum A[j]
that A[i] + A[j] <= target.

For each elements in the subarray A[i+1] ~ A[j],
we can pick or not pick,
so there are 2 ^ (j - i) subsequences in total.
So we can update res = (res + 2 ^ (j - i)) % mod.

We don't care the original elements order,
we only want to know the count of sub sequence.
So we can sort the original A, and the result won't change.


#Complexity

Time O(NlogN)
"""

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        count = 0
        nums.sort()
        _mod = int(1e9) + 7
        
        left = 0
        right = len(nums)-1
        
        while left <= right:
            if nums[left] + nums[right] <= target:
                count += pow(2, right - left, _mod)
                left+=1
            else :
                right-=1

        return count % _mod

