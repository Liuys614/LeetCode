class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        aeiou = "aeiou"
        mask = [0,0,0,0,0]
        ptr, ptr_w = 0, 0
        longestStr = ""
        
        while ptr < len(s):
            ptr_w = 0
            mask = [0,0,0,0,0]
            ss = s[ptr:]
            while ptr_w < len(ss):
                if ss[ptr_w] in aeiou:
                    mask[aeiou.find(ss[ptr_w])] ^= 1
                if (1 not in mask) and (len(ss[:ptr_w+1]) > len(longestStr)):
                    longestStr = ss[:ptr_w+1]
                ptr_w += 1
            ptr += 1
           
        return len(longestStr)



