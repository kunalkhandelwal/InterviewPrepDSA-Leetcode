#https://leetcode.com/problems/find-the-number-of-good-pairs-i/submissions/1375848661/



#Optimal Solution: Beats 68, 68
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans = 0
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]%(nums2[j]*k)==0:
                    ans+=1
        return ans

#Sol 0: Beats - 29, 18
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums2)):
            nums2[i] = nums2[i]*k
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]%nums2[j]==0:
                    ans+=1
        return ans

  
