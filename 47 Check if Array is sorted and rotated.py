#https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/
#Sol 0: Beats - 88, 75 , solved it under 2mins
class Solution:
    def check(self, nums: List[int]) -> bool:

        flag = 0
        for i in range(len(nums)):
            if nums[i-1]>nums[i]:
                flag += 1
            if flag >1:
                return False
        return True
