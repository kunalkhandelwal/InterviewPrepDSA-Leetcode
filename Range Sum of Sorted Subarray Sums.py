#Sol1: Beats: 23, 14
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        ans = []
        l = len(nums)
        k= 0
        for i in range(l):
            current_sum = 0
            for j in range(i, l):
                current_sum += nums[j]
                ans.append(current_sum)
        #print(ans)
        
        ans.sort()
        print(ans)

        for i in range(left-1, right):
            k+= ans[i]
        return (k%(10**9 + 7))

  #Sol 2: beats 74, 51
  class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        ans = []
        l = len(nums)
        k= 0
        for i in range(l):
            current_sum = 0
            for j in range(i, l):
                current_sum += nums[j]
                ans.append(current_sum)
        #print(ans)
        
        ans.sort()

        return(sum(ans[left-1:right])%(10**9+7))
