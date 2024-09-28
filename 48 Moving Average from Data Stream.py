#https://leetcode.com/problems/moving-average-from-data-stream/description/
#Sol 0: 
from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.deque = deque()
        self.window_sum = 0 

    def next(self, val: int) -> float:
        self.deque.append(val)
        self.window_sum += val

        if len(self.deque) > self.size:
            oldest_val = self.deque.popleft()
            self.window_sum -= oldest_val

        return self.window_sum / len(self.deque)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
