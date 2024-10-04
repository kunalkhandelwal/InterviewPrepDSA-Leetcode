#Sol 0: Beats - 69, 33
class Solution:
    def longestPalindrome(self, s: str) -> int:

        ans = 0
        d = {}
        oddFound = False
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1

        for value in d.values():
            if value%2 != 0:
                ans += value - 1
                oddFound = True

            else:
                ans+= value

        if oddFound:
            ans += 1

        return ans
