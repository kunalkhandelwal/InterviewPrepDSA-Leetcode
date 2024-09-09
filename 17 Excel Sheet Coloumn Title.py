#Sol 0: Beats- 9, 99
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""

        while columnNumber>0:
            ans += chr( ((columnNumber-1)%26) + 65)
            columnNumber//= 26

        return ans[::-1]
