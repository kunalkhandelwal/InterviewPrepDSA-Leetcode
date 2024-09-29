#Sol 0:
class Solution:
    def fib(self, n: int) -> int:
        while(n<=1):
            return n
        return self.fib(n-2) + self.fib(n-1)


#Sol 1: Beats - 91, 60
class Solution:
    def fib(self, n: int) -> int:
        if(n<=1):
            return n
        
        ans = [0]*(n+1)
        ans[1] = 1

        for i in range(2, n+1):
            ans[i] = ans[i-1] + ans[i-2]

        return ans[n]
