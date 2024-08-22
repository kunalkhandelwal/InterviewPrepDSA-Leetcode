#Sol 1: FUCK YEAHHHH, BEATS MEMORY- 99%, RUNTIME- 99% 
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:

        min_num = arrays[0][0]
        max_num = arrays[0][-1]
        max_distance = 0

        for array in arrays[1:]:

            min_num_array = array[0]
            max_num_array = array[-1]

            max_distance = max(max_distance, abs(max_num_array - min_num), abs(max_num - min_num_array))

            if max_num_array > max_num:
                max_num = max_num_array
            
            if min_num_array < min_num:
                min_num = min_num_array
        return max_distance

#Sol 0: 121/136 Test cases passed
#22min
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:

        min_num = float('inf')
        max_num = float('-inf')
        
        for array in arrays:
            val = 0
            min_num_array=0
            max_num_array=0

            min_num_array = array[0]
            max_num_array = array[-1]

            if max_num_array > max_num:
                max_num = max_num_array
            
            if min_num_array < min_num:
                min_num = min_num_array

        a1 = abs(min_num - max_num)
        a2 = abs(max_num - min_num)
        print(a1, a2)
