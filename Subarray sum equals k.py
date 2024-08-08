#https://leetcode.com/problems/subarray-sum-equals-k/description/

#OPTIMAL SOLUTION



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
