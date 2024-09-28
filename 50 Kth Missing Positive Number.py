#Sol 1: optimal solution - Used binary search
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l = 0
        r = len(arr)-1

        while l<=r:
            mid = (l+r)//2

            if arr[mid] - mid -1 < k: #most imp step of problem as helps finding MISSING COUNT
                l = mid + 1
            else:
                r = mid - 1

        return l+k

#Sol 0: beats 5,5
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l = []
        for i in range(1, arr[-1]+k+1):
            if i not in l and i not in arr:
                l.append(i)
        ans = l[k-1]
        return ans
