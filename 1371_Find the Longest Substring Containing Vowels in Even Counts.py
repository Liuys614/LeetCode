"""
## 如何取得題目要求的字串
合理的字串是，把從頭掃到目前的位置的母音奇偶狀態
扣掉之前紀錄過最早的值，就可以算出字串長度

## 資料結構Seen{母音奇偶狀態：最早出現的索引}
紀錄最早出現奇數個字母的位置
index使用bitmap來表示哪一個字母是奇數
```
00000：到目前為止偶數個母音
00001：有奇數個a
00011：有奇數個a和奇數個b
```
value為最早出現的位置

因為我們是要找最長的字串
所以這個value只會紀錄最靠近頭的，不必更新

初始化為{0:-1}的理解為
最早都是偶數個母音的位置在-1

## cur
目前的母音奇數狀態
"""

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        seen = {0:-1}
        maxStr = 0
        cur = 0
        for i,c in enumerate(s):
            cur ^= ( 1 << ("aeiou".find(c) + 1) ) >> 1
            seen.setdefault(cur,i)
            maxStr = max(maxStr, i - seen[cur])
        return maxStr

