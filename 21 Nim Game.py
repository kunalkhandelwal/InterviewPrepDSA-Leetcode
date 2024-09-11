class Solution:
    def canWinNim(self, n: int) -> bool:
        if n%4 != 0:
            return True
        return False

# Correct Solution:
# The problem can be solved with a very simple observation:

# If n % 4 == 0, you will lose.
# If n % 4 != 0, you can win.
# This is because if the number of stones is divisible by 4, no matter how many stones you remove (1, 2, or 3), 
# your opponent can always respond by removing stones in such a way that the number of stones left is still a multiple of 4. In this scenario, your opponent can always win.
