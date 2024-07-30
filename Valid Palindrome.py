#Sol 1: Took me 20mins will couple failed submissions.
class Solution:
    def isPalindrome(self, s: str) -> bool:

        d = ""
        s = s.lower()
        print(s)
        for i in range(len(s)):
            if (ord(s[i])>=65 and ord(s[i])<=90) or (ord(s[i])>=97 and ord(s[i])<=122) or (ord(s[i])>=48 and ord(s[i])<=57):
                d+=s[i]

        left = 0
        right= len(d)-1

        while(left<=right):
            if d[left]==d[right]:
                left+=1
                right-=1
            elif left==right:
                return True
            else:
                return False
        return True


class Solution:
    def isPalindrome(self, s: str) -> bool:

        d = ""
        s = s.lower()
        print(s)
        for i in range(len(s)):
            if (s[i].isalnum()):
                d+=s[i]

        left = 0
        right= len(d)-1

        while(left<=right):
            if d[left]==d[right]:
                left+=1
                right-=1
            elif left==right:
                return True
            else:
                return False
        return True
