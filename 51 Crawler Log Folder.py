#Sol 1:
#Beats: 66, 40
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for i in range(len(logs)):
            if logs[i] == "./":
                continue
            elif logs[i] == "../":
                if stack:
                    stack.pop()
                stack.append(logs[i])
        return len(stack)

#Sol 0: Beats - 75, 6
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        val = 0

        for i in range(len(logs)):
            if logs[i] == "./":
                continue
            elif val==0 and (logs[i] == "../" or logs[i] == "./"):
                continue                
            elif logs[i] == "../" and val!=0:
                val -= 1
            else:
                val+= 1
            print(val)

        if val<0:
            return 0
        else:
            return val

      #Sol 1: With Stack
      
