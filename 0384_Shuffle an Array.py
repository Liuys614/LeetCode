
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
        res = []
        tmp = self.ori.copy()
        for i in reversed(range(len(self.ori))):
            index = randint(0,i)
            res.append(tmp[index])
            tmp.pop(index)
        return res

