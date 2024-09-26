#Sol 0: 21min, Beats - 83, 32
class Solution:
    def specialArray(self, nums: List[int]) -> int:

        #x -> 0 to len(nums)
        #comparison should be done with every element in nums
        # if count>x or count<x: x+=1, count == x -> ans = max(ans, x)

        ans = 0

        for x in range(len(nums)+1):
            count = 0
            for i in range(len(nums)):
                if nums[i]>= x:
                    count+=1

                if count>x:
                    break
            if count == x:
                ans = max(ans, x)
        if ans == 0:
            return -1
        return ans
