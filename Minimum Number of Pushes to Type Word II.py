Beats: 5, 33
class Solution:
    def minimumPushes(self, word: str) -> int:

        d = {}

        for i in range(len(word)):
            if word[i] not in d:
                d[word[i]] = 1
            else:
                d[word[i]]+=1
        
        if len(d.keys())<=8:
            return len(word)
        elif len(d.keys())>8 and len(d.keys())<=26:
            sorted_d = dict(sorted(d.items(), key=lambda item: item[1], reverse = True))
        
        l = 1
        r = len(d.values())
        print(sorted_d)

        ans = 0

        for key, value in sorted_d.items():
            if l<=8:
                ans = ans + value
            elif l>8 and l<=16:
                ans = ans + (value*2)
            elif l>16 and l<=24:
                ans = ans + (value*3)
            else:
                ans = ans+ (value*4)
            l+=1
            print(ans, l)
        return ans
