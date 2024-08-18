#Sol 1: 42, 90

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        d = {}
        ans = []
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
        
        sorted_nums = sorted(nums, key = lambda x : (d[x], -x))

        return sorted_nums

  #Sol 2: 68, 57
  class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        d = Counter(nums)
        
        sorted_nums = sorted(nums, key = lambda x : (d[x], -x))

        return sorted_nums
