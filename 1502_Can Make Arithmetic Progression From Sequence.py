"""
使用set跟等差級數來解這個問題。

如果是n個等差級數，那所有數字減掉最小，再除以gap所形成的組合，應該要是0~n-1。
"""


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        m = min(arr)
        M = max(arr)
        eleSet = set()

        if m - M == 0:
            return True

        gap = (M - m)/(len(arr)-1)
        if gap%1:
            return False

        for n in arr:
            diff = (n-m)/gap
            if diff%1 :
                return False
            eleSet.add(diff)

        if len(eleSet) != len(arr):
            return False

        return True
