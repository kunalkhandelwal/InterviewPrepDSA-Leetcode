#Sol 1: Beats - 33, 42
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        max_num = ans = streak = 0

        for num in nums:
            if num > max_num:
                max_num = num
                ans = streak = 0

            if max_num == num:
                streak+=1
            else:
                streak = 0

            ans = max(streak, ans)
            
        return ans
