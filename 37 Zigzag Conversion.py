#https://leetcode.com/problems/zigzag-conversion/submissions/1397868561/?envType=study-plan-v2&envId=top-interview-150

#Sol 0:
class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if  numRows == 1 or numRows>= len(s):
            return s

        l = []
        ans = ""
        index = 0

        for i in range(numRows):
            l.append("")

        for i in range(len(s)):
            l[index] += s[i]

            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1

            index+= step

        for i in range(len(l)):
            ans += l[i]

        return ans
