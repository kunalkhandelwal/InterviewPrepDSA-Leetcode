#Sol 0: 10mins -Beats - 30, 30
#class Solution:
    def addDigits(self, num: int) -> int:
        ans = 0
        final_ans = 0

        while(num>0):
            ans = num%10
            final_ans += ans
            num = num//10
            if num == 0 and final_ans>=10:
                num = final_ans
                final_ans = 0

        return final_ans

#More optimal
Approach
# Base Case Check:
# If the input number num is 0, the result is 0 because the digital root of 0 is 0.
# Divisibility Check:
# If num is divisible by 9, return 9. This is because any number that is a multiple of 9 has a digital root of 9 (except for 0).
# General Case:
# For all other numbers, return num % 9. This remainder gives the digital root directly. This is based on the properties of numbers and modulo arithmetic, which simplifies the process to a constant-time solution.

#Sol 1: beats - 43, 31
        if num == 0:
            return 0
        if num%9==0:
            return 9
        else:
            return num%9

#Sol 2 - Beats - 37, 31
class Solution:
    def addDigits(self, num: int) -> int:
        while(len(str(num))>1):
            num = sum(int(i) for i in str(num))
        return num
