#https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/description/?envType=company&envId=workday&favoriteSlug=workday-all
#Sol 1 --> Brute Force- beats: 52, 75

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:

        ans = 0

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    ans+=1
        return ans

  #Sol 2:

