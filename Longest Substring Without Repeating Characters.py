# Sol 1 - Brute force - TLE
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        def check(start, end):
            chars = set()
            for i in range(start, end+1):
                c = s[i]
                if c in chars:
                    return False
                chars.add(c)
            return True

        n = len(s)
        res = 0

        for i in range(n):
            for j in range(i, n):
                if check(i,j):
                    res = max(res, j-i+1)
        return res

  #Sol 2:
  class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        ans = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            ans = max(ans, r-l+1)
        return ans
