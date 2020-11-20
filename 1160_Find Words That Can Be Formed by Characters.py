class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        for w in words:
            tmpChars = chars
            find = True
            if len(w) > len(chars):
                continue
            for c in w:
                if c not in tmpChars:
                    find = False
                    break
                else:
                    tmpChars = tmpChars.replace(c,'',1)
            if find != False and len(tmpChars):
                ans += len(w)
        return ans


