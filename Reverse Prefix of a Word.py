#Sol 1: 26min , Beats 75, 23

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ans = ""
        rev = ""
        val = 0
        r = 0

        while(r<len(word)):
            if val== 0:
                ans+=word[r]
            if val == 1:
                rev = rev + word[r]

            if word[r] == ch:
                rev ="" 
                rev = ans[::-1]
                val = 1
                ch=""
            print(rev)
            r+=1
        if rev =="":
            return word
        else:
            return rev

#Sol 2: Beats 35, 93
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ans = ""

        if ch not in word:
            return word
        if ch in word:
            i = word.index(ch)
        return(word[:i+1][::-1]+word[i+1:])

