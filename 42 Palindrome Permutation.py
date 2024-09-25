#https://leetcode.com/problems/palindrome-permutation/description/

Sol 0:
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        d = {}
        flag = 0
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1

        for key, value in d.items():
            if value%2 == 1:
                flag+=1

        if flag>1:
            return False
        else:
            return True

        
