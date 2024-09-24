#Sol 0: 3min, beats - 88, 19
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:

        for i in range(1, len(arr)-1):
            if arr[i-1]%2 != 0 and arr[i]%2 != 0 and arr[i+1]%2 != 0:
                return True
        return False


#Sol 1: Beats - 78, 65
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:

        count = 0
        for num in arr:
            if num%2 == 1:
                count+=1
                if count == 3:
                    return True
            else:
                count = 0
        return False
