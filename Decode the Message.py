#Sol1 : Beats 56, 20
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:

        key1 = ''.join(key.split())
        s = 'abcdefghijklmnopqrstuvwxyz'

        d = {}
        ans =''
        k=0
        for i in range(len(key1)):
            if key1[i] not in d:
                d[key1[i]] = s[k]
                k+=1
        
        for c in range(len(message)):
            if message[c]==" ":
                ans+= " "
            else:
                ans+= d[message[c]]
        return ans

#Sol 2: Beats: 44, 61
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:

        key1 = ''.join(key.split())
        s = 'abcdefghijklmnopqrstuvwxyz'

        d = {}
        ans =''
        k=0
        for i in range(len(key1)):
            if key1[i] not in d:
                d[key1[i]] = s[k]
                k+=1
                if k == 26:
                    break
        
        for c in range(len(message)):
            if message[c]==" ":
                ans+= " "
            else:
                ans+= d[message[c]]
        return ans
