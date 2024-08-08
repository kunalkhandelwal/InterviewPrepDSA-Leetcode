#https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/description/?envType=company&envId=workday&favoriteSlug=workday-all

#Actual Answer: OPTIMAL SOLUTION: Beats 88, 61 # We come to realize that all the numbers will be multiplied by their pairs but 0 and 30, and we will use n*(n-1)//2 formula to find the number of pairs for that. 
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans = 0
        arr = [0]*60

        for num in time:
            num = num%60
            arr[num]+=1

        for i in range(1, 30):
            ans+= (arr[i]*arr[60-i])

        ans+= ((arr[0])*(arr[0]-1))//2
        ans+= ((arr[30])*(arr[30]-1))//2 
        return ans



#Sol 1: TIME LIMIT EXCEEDED WHEN TRYING BRUTE FORCE SOLUTION - 30/35

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans = 0
        l=[]

        for i in range(len(time)):
            for j in range(i, len(time)):
                if ((time[i] + time[j])%60 == 0) and i<j:
                    ans+=1
                    l.append([i,j])
        return ans

# Sol 2: TIME LIMIT EXCEEDED WHEN USING WHILE LOOP - 29/35

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans = 0
        l,r = 0, len(time)-1

        while(l<r):

            if (time[l]+time[r])%60 == 0 and r>l:
                ans+=1
            r-=1

            if r==l and r<=len(time)-1:
                l+=1
                r=len(time)-1

            if l>=len(time)-1:
                break

        return ans
