#https://leetcode.com/problems/excel-sheet-column-number/description/

#Sol 1: Beats 88, 19
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        power = len(columnTitle)
        ans = 0
        for i in range(len(columnTitle)):
            ans += ( (ord(columnTitle[i]) - 64)*((26)**(power-1)) )
            power -= 1
        return ans

#Sol 0: Beats - 94, 19
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for i in range(len(columnTitle)):
            ans = 26 * ans
            ans += (ord(columnTitle[i]) - 64)
        return ans
