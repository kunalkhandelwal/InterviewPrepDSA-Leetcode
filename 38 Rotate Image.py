#https://leetcode.com/problems/rotate-image/?envType=study-plan-v2&envId=top-interview-150
Beats- 87, 46

#Sol 0:
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):

                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()

        return matrix
