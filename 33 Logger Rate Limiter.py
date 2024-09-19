#Sol 0: beats 95
class Logger:

    def __init__(self):
        self.message_timestamps = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.message_timestamps and timestamp - self.message_timestamps[message]<10:    
            return False
        else:
            self.message_timestamps[message] = timestamp
            return True


# Your Logger object will be instantiated and called as such:
obj = Logger()
print(obj.shouldPrintMessage(1, "foo"))
print(obj.shouldPrintMessage(2, "bar"))
print(obj.shouldPrintMessage(3, "foo"))
print(obj.shouldPrintMessage(8, "bar"))
print(obj.shouldPrintMessage(10, "foo"))
print(obj.shouldPrintMessage(11, "foo"))
