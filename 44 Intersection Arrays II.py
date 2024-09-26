#Sol 0: beats - 40, 35
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        d1 = {}
        ans = []

        for num in nums1:
            if num not in d1:
                d1[num] = 1
            else:
                d1[num] += 1

        for num in nums2:
            if num in d1 and d1[num] > 0:
                ans.append(num)
                d1[num] -= 1
        return ans

  #Sol 1:beats - 40, 8
  class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        d1 = Counter(nums1)
        ans = []

        for num in nums2:
            if num in d1 and d1[num] > 0:
                ans.append(num)
                d1[num] -= 1
        return ans

    #Sol 2:
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        i,j,k = 0,0,0

        ans = []

        while (i<len(nums1) and j<len(nums2)):
            if nums1[i] < nums2[j]:
                i+=1
            elif nums1[i] > nums2[j]:
                j+=1
            else:
                ans.append(nums1[i])
                i+=1
                j+=1
        return ans
