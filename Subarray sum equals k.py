#https://leetcode.com/problems/subarray-sum-equals-k/description/

#OPTIMAL SOLUTION - Beats - 69, 53
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        prefix_sum = 0
        d = {0:1}

        for num in nums:

            prefix_sum = prefix_sum + num

            if (prefix_sum - k) in d:
                ans = ans + d[prefix_sum - k]
            if (prefix_sum) not in d:
                d[prefix_sum] = 1
            else:
                d[prefix_sum] = d[prefix_sum] + 1
        return ans


#Sol 1: TIME LIMIT EXCEEDED

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        ans = 0

        for i in range(len(nums)):
            subsum = 0
            # if nums[i]==k:
            #     ans+=1
            for j in range(i, len(nums)):
                subsum+=nums[j]

                if subsum ==k:
                    #print(i,j)
                    ans+=1
        return ans
