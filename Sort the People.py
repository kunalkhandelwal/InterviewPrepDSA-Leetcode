#Sol 1: Beats - 67, 27
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        d = {}
        for i in range(len(heights)):
            d[heights[i]]=names[i]
        #print(d)
            
        
        ans = dict(sorted(d.items(), key=lambda item: item[0], reverse = True))
        return(ans.values())
