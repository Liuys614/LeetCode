"""
    1.一個指針去指向下一次要增加幾個數字參考的地方
    2.使用xor 3 來切換1,2
"""

class Solution:
    def magicalString(self, n: int) -> int:
        array=[1,2,2,1,1]
        cur_num = 2 #number ready to be append
        ptr_num = 3 #counts of numbers ready to be append
        while len(array) <= n:
            if array[ptr_num] == 1:
                array.append(cur_num)
            else:
                array.append(cur_num)
                array.append(cur_num)
            cur_num ^= 3 #fancy way for change 1 & 2 (xor 3)
            ptr_num += 1
        return array[:n].count(1)
        
        
