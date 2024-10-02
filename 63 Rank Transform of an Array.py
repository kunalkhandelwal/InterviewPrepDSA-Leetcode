#Sol 1: Beats - 53, 61
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        ranks = {}

        nums = sorted(list(set(arr)))
        
        for i in range(len(nums)):
            ranks[nums[i]] = i+1

        for i in range(len(arr)):
            arr[i] = ranks[arr[i]]

        return arr

#Sol 0: Beats - 18, 75
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        nums = arr.copy()
        l = []
        arr.sort()
        d = {}

        flag = 0
        
        for i in range(len(arr)):
            if arr[i] not in d:
                d[arr[i]] = flag+1
                flag += 1

        
        for i in range(len(nums)):
            l.append(d[nums[i]])

        return l

