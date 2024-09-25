class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        ans = []
        s1 = set(nums1)
        s2 = set(nums2)
        for num in s1:
            if num in s2:
                ans.append(num)
        return ans
