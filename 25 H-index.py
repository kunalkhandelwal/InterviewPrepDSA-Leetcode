#Sol 0: Beats - 91, 14
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        if max(citations) == 0:
            return 0
        
        if len(citations) == 1 and citations[0] < 1:
            return 0
        if len(citations) == 1 and citations[0] >= 1:
            return 1

        citations.sort()
        citations = citations[::-1]

        for i in range(len(citations)):
            if citations[i] >= i+1:
                h = i+1
        return h
