Beats 90, 65

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1]!=nums[i]:
                self.twoSumII(nums, i , ans)
        return ans

    def twoSumII(self, nums: List[int], i: int, ans:List[List[int]]):
        l, r = i+1, len(nums) - 1

        while l<r:

            sum = nums[i] + nums[l] + nums[r]

            if sum<0:
                l+= 1
            elif sum > 0:
                r-=1
            else:
                ans.append([nums[i], nums[l], nums[r]])
            
                l+=1
                r-=1
                while l<r and nums[l]==nums[l-1]:
                    l+=1
