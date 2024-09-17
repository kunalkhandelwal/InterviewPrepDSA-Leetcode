#Sol 0: took me 15
#Beats - 89, 79

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        s = ""
        s = s1 + " " + s2
        l = []
        l.append(s.split(" "))
        d = {}
        ans = []

        l1 = l[0]
       
        for i in range(len(l1)):
            if l1[i] not in d:
                d[l1[i]] = 1
            else:
                d[l1[i]] += 1

        for key, value in d.items():
            if value == 1:
                ans.append(key)

        return ans
