#Sol 0:
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        l = []

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                l.append(nums[i])
        
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                l.append(nums[i])

        return l

#Sol 1: More optimal  Beats - 77, 60
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        l = 0

        for r in range(len(nums)):
            if nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
        return nums

  
