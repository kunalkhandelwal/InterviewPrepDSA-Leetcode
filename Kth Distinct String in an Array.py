#Sol 1: Beats - 51, 75
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        d = {}
        print(len(arr))

        for i in range(len(arr)):
            if arr[i] not in d:
                d[arr[i]]=1
            else:
                d[arr[i]]+=1
        #print(d)
        for s in d:
            if d[s]==1:
                k-=1
                if k==0:
                    return s
        return ""

  #Sol 2:
  
