#Sol 0 - Beats - 78, 24, solved in less than 10min
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:

        k = k% sum(chalk)

        if k == 0:
            return 0

        for i in range(len(chalk)):
            if chalk[i] > k:
                return i

            k = k - chalk[i]

            if k < 0:
                return i
