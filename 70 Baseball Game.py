#Sol 0: Beats - 87, 47
class Solution:
    def calPoints(self, ops: List[str]) -> int:

        stack = []

        for i in range(len(ops)):
            if not stack:
                stack.append(int(ops[i]))
            elif ops[i] == "+":
                stack.append(stack[-1]+stack[-2])
            elif ops[i] == 'C':
                stack.pop()
            elif ops[i] == 'D':
                stack.append(2*stack[-1])
            else:
                stack.append(int(ops[i]))

        return sum(stack)
