#https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/?envType=daily-question&envId=2024-09-11

#Sol 0: Beats : 97, 27
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        
        ans = 0
        start = bin(start)[2:]
        goal = bin(goal)[2:]

        if len(start) > len(goal):
            for i in range(len(start)-len(goal)):
                goal = "0" + goal

        elif len(start) < len(goal):
            for i in range(len(goal)-len(start)):
                start = "0" + start

        for i in range(len(goal)):
            if start[i]!= goal[i]:
                ans+=1
        return ans
