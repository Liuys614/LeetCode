
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        # X_Y : x in s1, y in s2, with same index
        # Y_X : y in s1, x in s2, with same index
        X_Y, Y_X, res = 0, 0, 0
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            if s1[i] == "x" and s2[i] == "y":
                X_Y += 1
            else:
                Y_X += 1

        # swap by "xx"<=>"yy" or "yy"<=>"xx"
        res += X_Y//2
        X_Y = X_Y%2
        res += Y_X//2
        Y_X = Y_X%2

        # swap by "xy"<=>"yx" or "yx"<=>"xy"
        tmp = min(X_Y,Y_X)
        res += tmp * 2
        X_Y -= tmp
        Y_X -= tmp

        return res if X_Y == 0 and Y_X == 0 else -1
