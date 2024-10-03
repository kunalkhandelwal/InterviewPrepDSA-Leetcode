#Sol 0:
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        d = {}
        max_value = float('-inf')
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1

        for key, value in d.items():
            if key > max_value and value == 1:
                max_value = max(key, max_value)
        if max_value>0:
            return max_value
        else:
            return -1
