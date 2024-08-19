#Sol 1- Beats 66, 5
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        d = {}
        ans = 0
        max_val = 0
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        
        l = list(d.values())
        l1 = l.sort(reverse=True)
        max_val = l[0]

        for val in l:
            if val>=max_val:
                ans+= val
        return ans

  #Sol 2: Beats - 99, 94
  class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        d = {}

        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        
        max_freq = 0
        for value in d.values():
            max_freq = max(max_freq, value)
        
        num_of_max_freq = 0
        for val in d.values():
            if val == max_freq:
                num_of_max_freq +=1 
        return max_freq*num_of_max_freq
