#Actual Solution - Sliding Window:Beats: 88, 87
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        window = set()
        L = 0
        for r in range(len(nums)):
            if (r-L) > k:
                window.remove(nums[L])
                L += 1
            if nums[r] in window:
                return True
            window.add(nums[r])

        return False


#Sol 0: 
#Beats - 33, 71
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        index_map = {}

        for i in range(len(nums)):
            num = nums[i]

            if num in index_map and i - index_map[num] <= k:
                return True
            
            index_map[num] = i
            
        return False
