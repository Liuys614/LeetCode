class Solution:

    def __init__(self, nums: List[int]):
        self.ori = nums.copy()

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.ori
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        res = self.ori.copy()
        for i in reversed(range(len(self.ori))):
            j = randint(0,i)
            res[i], res[j] = res[j], res[i]
            
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
