class Logger:

    def __init__(self):
        self.lastPrinted = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.lastPrinted:
            self.lastPrinted[message] = timestamp
            return True
        if self.lastPrinted[message] <= timestamp - 10:
            self.lastPrinted[message] = timestamp
            return True
        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)