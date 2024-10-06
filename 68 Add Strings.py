#https://leetcode.com/problems/add-strings/?envType=problem-list-v2&envId=math&difficulty=EASY
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        ans = []

        carry = 0
        p1 = len(num1) - 1
        p2 = len(num2) - 1

        while p1>=0 or p2>=0:
            x1 = ord(num1[p1]) - ord('0')  if p1>=0 else 0
            x2 = ord(num2[p2]) - ord('0')  if p2>=0 else 0

            value = (x1+x2+carry)% 10
            carry= (x1+x2+carry)// 10
            ans.append(value)

            p1-=1
            p2-=1

        if carry:
            ans.append(carry)

        return ''.join(str(x) for x in ans[::-1])
