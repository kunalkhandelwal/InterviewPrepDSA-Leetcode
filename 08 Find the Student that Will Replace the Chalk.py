#Actual Solution of the question:



#Sol 0: TLE - 20/72
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:

        ind = 0
        i = 0

        while(k>0):
                    
            k = k - chalk[i]

            if k <= 0 and i!= len(chalk)-1:
                return i
            elif k <= 0 and i== len(chalk)-1:
                return 0

            if i!= len(chalk)-1:
                i+=1
            else:
                i = 0
