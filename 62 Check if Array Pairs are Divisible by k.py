#Sol 0: Beats - 41, 59
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        remainder_count = defaultdict(int)

        for i in range(len(arr)):
            remainder = arr[i] % k

            if remainder< 0:
                remainder += k
            remainder_count[remainder] += 1

        print(remainder_count)

        for remainder in remainder_count:
            if remainder == 0:
                if remainder_count[remainder]%2 != 0:
                    return False

            else:
                if remainder_count[remainder] - remainder_count[k-remainder] != 0:
                    return False

        return True

  
