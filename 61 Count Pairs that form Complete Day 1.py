#Sol 0: Beats - 86, 5
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        
        ans= 0
        for i in range(len(hours)):
            for j in range(i, len(hours)):
                if (hours[i] + hours[j]) % 24 == 0 and i<j:
                    ans += 1
        return ans

  #Sol 1: Beats - 86, 16 (More optimal)
  class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        
        count = 0
        d = defaultdict(int)

        for hour in hours:
            remainder = hour%24

            if remainder == 0:
                count += d[0]
            else:
                count += d[24- remainder]

            d[remainder] += 1

        return count
