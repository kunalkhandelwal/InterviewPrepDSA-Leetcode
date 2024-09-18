#Sol 2: Beats 92, 65
  class Solution:
    def isStrobogrammatic(self, num: str) -> bool:

        ans = []

        for c in reversed(num):
            if c in {'0', '1', '8'}:
                ans.append(c)
            elif c == '6':
                ans.append('9')
            elif c == '9':
                ans.append('6')
            else:
                return False

        final_ans = "".join(ans)

        return final_ans == num

#Sol 1: beats - 36, 20
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:

        ans = ""

        for i in range(len(num)-1, -1, -1):
            if num[i] in {'0', '1', '8'}:
                ans+= num[i]
            elif num[i] == '6':
                ans+= '9'
            elif num[i] == '9':
                ans+= '6'
            else:
                return False

        return num == ans

  
