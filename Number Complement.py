#Sol 1: 14, 89
class Solution:
    def findComplement(self, num: int) -> int:
        binary_num = bin(num)[2:]

        comp = ''.join('1' if bit=='0' else '0' for bit in binary_num)

        return(int(comp, 2))

  #Sol 2: Beats: 78, 58
  class Solution:
    def findComplement(self, num: int) -> int:
        binary_num = bin(num)[2:]
        complement = ""
        for bit in binary_num:
            if bit == '1':
                complement+= '0'
            else:
                complement+= '1'
        return(int(complement, 2)) # This is used to convert a string which is in binary - "010" to a number = 2
