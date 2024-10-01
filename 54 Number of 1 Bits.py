class Solution:
    def hammingWeight(self, n: int) -> int:
        d = (bin(n)[2:])

        ans  = 0
        for i in range(len(d)):
            if d[i] == '1':
                ans+=1
        return ans
