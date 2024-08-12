#https://leetcode.com/problems/kth-largest-element-in-an-array/

#Sol 1:


#Sol : Beats: 66, 83 (But the question asked me to sort without using sorting, so trying again)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums.sort()
        return(nums[-k])


