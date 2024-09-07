#https://leetcode.com/problems/missing-ranges/description/?envType=problem-list-v2&envId=array&difficulty=EASY

#Sol 1: Beats - 8, 96
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:

        ans = []
        for a in nums+[upper+1]:
            if a > lower:
                ans.append([lower, a-1])        
            lower = a+1
        return ans

#Sol 0: Beats - 77, 78
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:

        ans = []  
        l = nums+[upper+1] # Took a little bit more space but reduced doing the math when iterating in a for loop
        for a in l:
            if a > lower:
                ans.append([lower, a-1])        
            lower = a+1
        return ans
