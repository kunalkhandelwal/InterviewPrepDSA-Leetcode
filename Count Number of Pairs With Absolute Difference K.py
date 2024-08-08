#https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/description/?envType=company&envId=workday&favoriteSlug=workday-all

#Optimal Solution: Beats 76, 32 #here we are using defaultdict because when using defaultdict, we can declare elements which don't even exist in the dictionary

"""
Dictionary (dict)
A standard dictionary in Python raises a KeyError if you try to access or modify a key that does not exist.
You have to explicitly check if a key exists before accessing or modifying it, or handle the KeyError.

Default Dictionary (defaultdict)
defaultdict is a subclass of dict from the collections module.
When you try to access or modify a key that does not exist, it automatically creates the key with a default value specified when the defaultdict was created.
You specify a default factory function (like int, list, etc.) when creating a defaultdict.
"""
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:

        ans = 0
        seen = defaultdict(int)

        for num in nums:
            ans+= seen[num-k] + seen[num+k]
            seen[num]+=1
        return ans


#Sol 1 --> Brute Force- beats: 52, 75

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:

        ans = 0

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    ans+=1
        return ans

  #Sol 2: Beats: 8, 75
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:

        ans = 0
        i,j = 0,1        
        l = len(nums)-1

        while(i<l):            
            if j==l+1:
                i+=1
                j = i
            if abs(nums[i] - nums[j]) == k:
                ans+=1
            j+=1
        return ans

