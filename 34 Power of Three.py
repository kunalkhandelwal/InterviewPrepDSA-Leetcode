#Sol 2: beats - 94
class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        if n<=0:
            return False
        
        while(n%3==0):
                n = n//3
        return n==1

#Sol 1: beats - 43, 8
class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        if n<=0:
            return False
        
        if n == 1:
            return True
        
        while(n>0):
            if n%3!=0:
                return False
            else:
                n = n//3
                if n == 1:
                    return True
        return True

#Sol 0: Beats - 21, 8, took me 8min
class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        if n<=0:
            return False
        
        if n == 1:
            return True
        

        n1 = n
        while(n>0):
            if n%3!=0:
                return False
            else:
                n1 = n//3
                print(n1)
                n = n1
                if n1 == 1:
                    return True
        return True
