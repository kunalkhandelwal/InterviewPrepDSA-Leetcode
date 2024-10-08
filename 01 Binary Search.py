#https://leetcode.com/problems/binary-search/

#Sol 1:
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        mid = 0

        while(l<=r):
            mid = ((l+r)//2)

            if nums[mid] == target:
                return mid
            elif target< nums[mid]:
                r = mid -1
            else:
                l = mid+1
        return -1
