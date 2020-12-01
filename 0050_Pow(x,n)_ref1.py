class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: 
            return 1
        
        if n < 0:
            x = 1/x
            n = -n
            return self.myPow(x,n)
        
        if n % 2:
            return x * self.myPow(x*x,n//2)
        
        return self.myPow(x*x,n/2)


