class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        if len(digits)<2 and digits[0]!=9:
            digits[0] +=1
            return digits
        
        if digits[-1] != 9:
            digits[-1]+=1
            return digits
        else:
            for i in range(len(digits)-1, -1, -1):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i]+=1
                    return digits
            return[1]+digits
