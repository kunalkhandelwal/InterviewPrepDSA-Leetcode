#https://leetcode.com/problems/missing-ranges/description/?envType=problem-list-v2&envId=array&difficulty=EASY

#Sol 1: Beats - 8, 96
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:

        ans = []
        for a in nums+[upper+1]:
            if a > lower:
                ans.append([lower, a-1])        
            lower = a+1            # We are doing lower = a+1 because we will go to the next: 
                                    """Input: nums = [0,1,3,50,75], lower = 0, upper = 99  ,  Output: [[2,2],[4,49],[51,74],[76,99]]"""
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
