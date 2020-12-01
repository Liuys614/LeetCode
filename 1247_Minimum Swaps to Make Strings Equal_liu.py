


class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        res = 0
        s1 = list(s1)
        s2 = list(s2)
        rm = list()

        # remove same char
        for i, c in enumerate(s1):
            if s1[i] == s2[i]:
                rm.append(i)
        for i in sorted(rm, reverse=True):
            del s1[i], s2[i]

        # for each char find s1="xx"/"yy" s2="yy"/"xx", and remove it
        find = True
        while find:
            find = False
            for i, c in enumerate(s1):
                for j, d in enumerate(s1[i+1:]):
                    if c == d and s2[i] == s2[j+i+1]:
                        del s1[j+i+1], s2[j+i+1], s1[i], s2[i]
                        res += 1
                        find = True
                        break

        # for each char find s1="xy"/"yx" s2="yx"/"xy", and remove it
        find = True
        while find:
            find = False
            for i, c in enumerate(s1):
                for j, d in enumerate(s1[i+1:]):
                    if c != d and s2[i] != s2[j+i+1]:
                        del s1[j+i+1], s2[j+i+1], s1[i], s2[i]
                        res += 2
                        find = True
                        break

        # if string not empty return -1 else return count's of moves
        return res if len(s1)==0 and len(s2)==0 else -1

