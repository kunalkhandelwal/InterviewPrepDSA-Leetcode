#https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/

#Sol 1: More optimal - beats - 68.91, 27
class Solution:
    def removeDuplicates(self, s: str) -> str:

        stack = []

        for i in s:
            if stack and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)

#Sol 0:
class Solution:
    def removeDuplicates(self, s: str) -> str:

        stack = []
        i = 0

        while(i<len(s)):
            if len(stack)!= 0 and stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
            i+=1
        return ''.join(stack)

