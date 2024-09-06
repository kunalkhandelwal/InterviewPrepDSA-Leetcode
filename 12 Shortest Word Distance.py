#https://leetcode.com/problems/shortest-word-distance/description/?envType=problem-list-v2&envId=array&difficulty=EASY

#Sol 1: More Optimal : O(n), O(1)
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:

        p1 = -1
        p2 = -1

        ans = len(wordsDict)

        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                p1 = i
            elif wordsDict[i] == word2:
                p2 = i
        
            if p1 != -1 and p2!=-1:
                ans = min(ans, abs(p1-p2))
        return ans

  #Sol 2:
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        w1 = []
        w2 = []

        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                w1.append(i)
            if wordsDict[i] == word2:
                w2.append(i)

        ans = 999999

        for i in range(len(w1)):
            for j in range(len(w2)):
                if ans> abs(w1[i]-w2[j]):
                    ans = abs(w1[i]-w2[j])
        return ans
        
  
