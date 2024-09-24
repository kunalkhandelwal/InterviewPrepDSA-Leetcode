#Sol 0: - Beats - 90, 15
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:

        num_columns = len(matrix[0])
        max_columns = [max(row[i] for row in matrix) for i in range(num_columns)]

        min_columns = []
        for row in matrix:
            min_columns.append(min(row))

        for i in range(len(max_columns)):
            if max_columns[i] in min_columns:
                return [max_columns[i]]
