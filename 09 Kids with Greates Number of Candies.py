#https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75\

#Sol 0: Beats - 73, 29
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        currMax = max(candies)
        l = [False]*len(candies)

        for i in range(len(l)):
            if candies[i] + extraCandies >= currMax:
                l[i] = True
        return l

#Sol 1: Beats - 13, 80
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = 0
        temp = 0
        l = []
        currMax = max(candies)

        for i in range(len(candies)):
            temp = candies[i] + extraCandies

            if temp>=currMax:
                l.append(True)

            else:
                l.append(False)
        return l
