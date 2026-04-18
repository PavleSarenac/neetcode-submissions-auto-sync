class MinHeap:
    
    def __init__(self):
        self.minHeap = [0]

    def push(self, val: int) -> None:
        self.minHeap.append(val)
        lastElementIndex = len(self.minHeap) - 1
        self.percolateUp(lastElementIndex)

    def pop(self) -> int:
        isHeapEmpty = len(self.minHeap) <= 1
        if isHeapEmpty:
            return -1
        minElementIndex = 1
        lastElementIndex = len(self.minHeap) - 1
        minValue = self.minHeap[minElementIndex]
        self.swap(minElementIndex, lastElementIndex)
        self.minHeap.pop()
        self.percolateDown(minElementIndex)
        return minValue

    def top(self) -> int:
        isHeapEmpty = len(self.minHeap) <= 1
        if isHeapEmpty:
            return -1
        return self.minHeap[1]

    def heapify(self, nums: List[int]) -> None:
        self.minHeap += nums
        lastNodeWithChildrenIndex = len(nums) // 2
        parentIndex = lastNodeWithChildrenIndex
        while parentIndex >= 1:
            self.percolateDown(parentIndex)
            parentIndex -= 1

    def percolateDown(self, nodeIndex: int):
        parentIndex = nodeIndex
        leftChildIndex = parentIndex * 2
        rightChildIndex = leftChildIndex + 1
        while leftChildIndex < len(self.minHeap):
            if self.minHeap[leftChildIndex] < self.minHeap[parentIndex] and (rightChildIndex >= len(self.minHeap) or self.minHeap[leftChildIndex] < self.minHeap[rightChildIndex]):
                self.swap(parentIndex, leftChildIndex)
                parentIndex = leftChildIndex
                leftChildIndex = parentIndex * 2
                rightChildIndex = leftChildIndex + 1
            elif rightChildIndex < len(self.minHeap) and self.minHeap[rightChildIndex] < self.minHeap[parentIndex]:
                self.swap(parentIndex, rightChildIndex)
                parentIndex = rightChildIndex
                leftChildIndex = parentIndex * 2
                rightChildIndex = leftChildIndex + 1
            else:
                break


    def percolateUp(self, nodeIndex: int):
        childIndex = nodeIndex
        parentIndex = childIndex // 2
        while parentIndex >= 1 and self.minHeap[childIndex] < self.minHeap[parentIndex]:
            self.swap(parentIndex, childIndex)
            childIndex = parentIndex
            parentIndex //= 2

    def swap(self, parentIndex: int, childIndex: int):
        tmp = self.minHeap[parentIndex]
        self.minHeap[parentIndex] = self.minHeap[childIndex]
        self.minHeap[childIndex] = tmp