class Solution:
    def isHappy(self, n: int) -> bool:

        s = set()

        def isSquare(n):
            total_sum = 0
            while(n>0):
                digit = n%10
                total_sum+= (digit**2)
                n = n//10
            return total_sum

        while n!=1 and n not in s:
            s.add(n)
            n = isSquare(n)
        return n==1
