#Sol 0: Beats - 75, 52
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        s = set()

        for num in nums:
            start = num[0]
            end = num[1]
            for j in range(start, end+1):
                s.add(j)
        return len(s)

  #Sol 1: Beats 81, 53
  class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        s = set()
        for start, end in nums:
            s|= set(range(start, end+1))
        return len(s)
