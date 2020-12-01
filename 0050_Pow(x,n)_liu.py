class Solution:
    def __init__(self):
        self.ch={}
    def myPow(self, x: float, n: int) -> float:
        if n in self.ch:
            return self.ch[n]
        
        if n == 0 or n==1 or n==-1 or n==2 or n==-2:
            self.ch[0]=1.0
            self.ch[1]=x
            self.ch[-1]=1/x
            self.ch[2]=x*x
            self.ch[-2]=(1/x)*(1/x)
            return self.ch[n] 
        
        #find lower and maximan number which is power of 2
        num = 2
        while(num*2 < abs(n)):
            num *= 2
        num = -num if n<0 else num
        
        res = self.myPow(x,num) * self.myPow(x,n-num)
        self.ch[n]= res
        return res
