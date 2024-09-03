#https://leetcode.com/problems/reshape-the-matrix/

#Sol: Beats- 85, 52
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        temp = []
        ans = []

        if len(mat)*len(mat[0])!=r*c:
            return mat

        for l in mat:
            for j in range(len(l)):
                temp.append(l[j])
        
        for i in range(r):
            ans.append(temp[i*c: (i+1)*c])
        return ans
