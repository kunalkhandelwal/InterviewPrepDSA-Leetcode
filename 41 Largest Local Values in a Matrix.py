#Sol 0:
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

        n = len(grid)

        result = [0]*(n-2)

        for i in range(0, n-2):
            result[i] = [0]*(n-2)

        for i in range(0, n-2):
            for j in range(0, n-2):

                curr_max = 0

                for k in range(0, 3):
                    for l in range(0, 3):
                        if curr_max < grid[i+k][j+l]:
                            curr_max = grid[i+k][j+l]


                result[i][j] = curr_max

        return result
