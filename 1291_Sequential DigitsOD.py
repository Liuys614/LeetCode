

class Solution:
    def sequentialdgs(self, low: int, high: int) -> List[int]:
        res = []
        dgs = int(math.log(low,10)) + 1 # digits count
        fdg = low // 10**(dgs-1)        # first digit
        while True:
            num = 0
            if fdg + dgs > 10:
                fdg = 1
                dgs += 1

            for i in range(dgs):
                num += (fdg+i)*(10**(dgs-i-1))

            if num > high:
                break

            if num < low:
                fdg += 1
                continue

            res.append(num)
            fdg += 1

        return res


