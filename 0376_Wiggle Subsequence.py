"""
- 因為連續上揚/下降，中間的點都可以忽略，所以只要判斷這一次的上或下即可
- 利用cntUp, cntDown 保留到目前為止，尾巴是上揚還是下垂的最長長度
- 每個新增加的點，只要判斷增加上去，是否可以增長長度，然後並更新長度即可
"""


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        cntUp, cntDown = 0, 0

        if len(nums) < 2:
            return len(nums)

        for i in range(len(nums)):
            if i == 0:
                cntUp, cntDown = 1, 1
                continue

            diff = nums[i] - nums[i-1]
            if diff > 0:
                cntUp = cntDown + 1
            elif diff < 0:
                cntDown = cntUp + 1

        return max(cntUp, cntDown)
