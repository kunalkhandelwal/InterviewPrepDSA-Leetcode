FINAL ANS: beats 88, 66
class Solution:
    def maxArea(self, height: List[int]) -> int:
        """[i, 0], [i, len(height)]"""
        h = 0
        b = 0
        l, r = 0, len(height)-1
        area = 0
        maxArea = 0

        while(l<=r):
            h = min(height[l], height[r])
            #print(h, "queen")
            b = r-l
            area = b*h
            #print(area, maxArea)
            if area>=maxArea:
                maxArea = area        
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxArea


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """[i, 0], [i, len(height)]"""
        h = 0
        b = 0
        l, r = 0, len(height)-1
        area = 0
        maxArea = 0

        while(l<=r):
            h = min(height[l], height[r])
            #print(h, "queen")
            b = r-l
            area = b*h
            #print(area, maxArea)
            if area>=maxArea:
                maxArea = area        
            l+=1
            if l==r:
                l=0
                r-=1
        return maxArea

  10 test cases didn't pass. 52/62

