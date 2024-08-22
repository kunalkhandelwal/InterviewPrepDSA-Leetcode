#https://leetcode.com/problems/lemonade-change/description/?envType=daily-question&envId=2024-08-22

#Sol 1: Beats - 77, 93 
#10min - Greedy
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for i in range(len(bills)):
            if bills[i] == 5:
                five+=1
            elif bills[i] == 10:
                ten+=1
                five-=1
            else:
                if ten>0:
                    ten-=1
                    five-=1
                else:
                    five-=3
                    
            if ten<0 or five<0:
                return False
        
        return True
