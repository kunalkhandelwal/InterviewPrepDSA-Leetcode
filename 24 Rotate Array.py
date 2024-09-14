#More optimal: Not using extra space 
#Sol 2:
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k%= n
        
        start = count = 0

        while count<n:
            current, prev = start, nums[start]
            while True:
                idx = (current + k)%n
                prev, nums[idx] = nums[idx], prev
                count+=1
                current = idx

                if start == current:
                    break
            start += 1

#Sol 0:
#Solved all by myself w/o help
#Not most optimal - beats - 5, 24

class Solution:
    def rotate(self, nums: List[int], k: int) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)

        if k == 0:
            return nums
        
        l = len(nums)
        nums_copy = []
        
        for i in range(len(nums)):
            nums_copy.append(nums[i])


        for i in range(l):
            nums.append(nums_copy[-k+i])

        for i in range(len(nums_copy)):
            nums.pop(0)
        
        return nums

  #Sol 1: optimally using extra space - beats - 77, 66
  class Solution:
    def rotate(self, nums: List[int], k: int) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n

        a = [0]*n

        for i in range(n):
            a[(i+k)%n] = nums[i]
            
        nums[:] = a
