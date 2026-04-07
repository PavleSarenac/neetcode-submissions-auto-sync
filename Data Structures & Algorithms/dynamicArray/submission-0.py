class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arraySize = 0
        self.array = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.arraySize == self.capacity:
            self.resize()
        self.array[self.arraySize] = n
        self.arraySize += 1

    def popback(self) -> int:
        self.arraySize -= 1
        return self.array[self.arraySize]

    def resize(self) -> None:
        oldArray = [0] * self.arraySize
        for i in range(self.arraySize):
            oldArray[i] = self.array[i]

        self.capacity *= 2
        self.array = [0] * self.capacity
        for i in range(self.arraySize):
            self.array[i] = oldArray[i]

    def getSize(self) -> int:
        return self.arraySize
    
    def getCapacity(self) -> int:
        return self.capacity
