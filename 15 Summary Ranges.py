#https://leetcode.com/problems/summary-ranges/description/?envType=study-plan-v2&envId=top-interview-150

Optimal Solution: Beats - 60,68 
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []

        i = 0

        while(i<len(nums)):
            start = nums[i]

            while i+1<len(nums) and nums[i]+1 == nums[i+1]:
                i+=1
            
            if start != nums[i]:
                ans.append(f"{start}->{nums[i]}")
            else:
                ans.append(str(nums[i]))
            
            i+=1
        return ans

#Sol 0:
#Beats - 39, 26.took me a very long time to write this
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        if not nums:
            return []
        
        start = float('-inf')
        ans = []

        for i in range(1, len(nums)):

            if nums[i] - nums[i-1] != 1 and start == float('-inf'):
                ans.append(str(nums[i-1])) 
                start = float('-inf') 

            elif nums[i] - nums[i-1] != 1 and start != float('-inf'):
                ans.append(f"{start}->{nums[i-1]}")
                start = float('-inf')

            elif nums[i] - nums[i-1] == 1 and start == float('-inf'):
                start = nums[i-1]

        if start!= float('-inf'):
            ans.append(f"{start}->{nums[-1]}")
        else:
            ans.append(str(nums[-1]))

        return ans

#Sol 1: Bakwaas editorial - beats 23, 26
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []

        i = 0

        while(i<len(nums)):
            start = nums[i]

            while i+1<len(nums) and nums[i]+1 == nums[i+1]:
                i+=1
            
            if start != nums[i]:
                ans.append(f"{start}->{nums[i]}")
            else:
                ans.append(str(nums[i]))
            
            i+=1
        return ans
