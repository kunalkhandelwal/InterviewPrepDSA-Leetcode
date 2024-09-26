#Sol 0: Beats - 97, 23
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        #[1,3,6,10,15]

        arr.sort()
        
        if len(arr)== 2:
            return [arr]

        ans = arr[1] - arr[0]
        l = []

        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            
            if diff==ans:
                ans = diff
                l.append([arr[i-1], arr[i]])
            elif diff<ans:
                ans = diff
                l = []
                l.append([arr[i-1], arr[i]])
        return l
