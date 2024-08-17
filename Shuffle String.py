#Sol 1: Beats - 9, 99
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d = {}
        ans = ""
        for i in range(len(indices)):
            d[indices[i]] = s[i]
        
        sorted_i = sorted(d.keys())
        for i in range(len(sorted_i)):
            ans+= d[i]
        return ans

#Sol 2: Beats: 56, 30
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = ""
        for i in range(len(s)):
            b = indices.index(i)
            ans += s[b]
        return ans
#Sol 3:
  class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = ""
        for i in range(len(s)):
            ans += s[indices.index(i)]
        return ans
