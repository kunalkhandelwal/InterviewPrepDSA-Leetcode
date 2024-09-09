
#Sol 1: beats: 19, 20

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones = 0
        zeroes = 0

        left = 0
        right = 0

        max_ones = -1

        for right in range(len(nums)):
            if nums[right] == 1:
                ones+=1
            if nums[right]== 0:
                zeroes+=1
            while zeroes>1:
                if nums[left] == 0:
                    zeroes-=1
                left+=1
            max_ones = max(right-left+1, max_ones)
        return max_ones
