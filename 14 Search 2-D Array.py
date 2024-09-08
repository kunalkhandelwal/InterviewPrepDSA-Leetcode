#Sol 0: Beats - 97, 65
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):

            if matrix[i][0]<=target<= matrix[i][-1]:

                # if matrix[i][0]==target:    They code on the side can be uncommented as well, it would just increase the run time and save a lot on the memory. 
                #     return True  

                # if matrix[i][-1]==target:
                #     return True

                l = 0
                r = len(matrix[0])-1

                while(l<=r):
                    mid = (l+r)//2

                    if matrix[i][mid] == target:
                        return True
                    elif target < matrix[i][mid]:
                        r = mid-1
                    else:
                        l = mid+1
            
        return False
