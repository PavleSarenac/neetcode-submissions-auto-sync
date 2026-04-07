class MyStack:

    def __init__(self):
        self.filledQueue = deque()
        self.emptyQueue = deque()

    def push(self, x: int) -> None:
        self.filledQueue.append(x)

    def pop(self) -> int:
        topValue = self.get_top_value()
        self.swap_queues()
        return topValue

    def top(self) -> int:
        topValue = self.get_top_value()
        self.emptyQueue.append(topValue)
        self.swap_queues()
        return topValue

    def empty(self) -> bool:
        return self.filledQueue.__len__() == 0
    
    def get_top_value(self) -> int:
        while self.filledQueue.__len__() > 1:
            self.emptyQueue.append(self.filledQueue.popleft())
        topValue = self.filledQueue.popleft()
        return topValue
    
    def swap_queues(self):
        tmp = self.filledQueue
        self.filledQueue = self.emptyQueue
        self.emptyQueue = tmp