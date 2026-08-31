class MinStack:

    def __init__(self):
        self.stack = []
        self.minvalue = []

    def push(self, val: int) -> None:
        if not self.minvalue:
            self.minvalue.append(val)
        else:
            self.minvalue.append(min(self.minvalue[-1], val))
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minvalue.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minvalue[-1]
