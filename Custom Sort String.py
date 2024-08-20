#Sol 1: Beats - 98, 95
# O(n+m), Time taken: 13mins
class Solution:
    def customSortString(self, order: str, s: str) -> str:

        d1 = {}
        d2 = {}

        ans = ""

        for i in range(len(order)): 
            d1[order[i]] = 1

        for j in range(len(s)):
            if s[j] not in d2:
                d2[s[j]] = 1
            else:
                d2[s[j]] += 1
            if s[j] not in d1:
                ans+= s[j]

        for key in d1.keys():
            if key in s:
                ans+= key*(d2[key])
        return ans
