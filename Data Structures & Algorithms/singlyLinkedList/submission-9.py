class ListNode:

    def __init__(self, val):
        self.value = val
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = self.tail = None
        self.listSize = 0

    def get(self, index: int) -> int:
        if index + 1 > self.listSize:
            return -1

        currentNode = self.head
        currentIndex = 0
        while currentIndex < index:
            currentNode = currentNode.next
            currentIndex += 1

        return currentNode.value

    def insertHead(self, val: int) -> None:
        newListNode = ListNode(val)
        newListNode.next = self.head
        self.head = newListNode
        if self.tail == None:
            self.tail = self.head
        self.listSize += 1

    def insertTail(self, val: int) -> None:
        newListNode = ListNode(val)
        if self.tail != None:
            self.tail.next = newListNode
        self.tail = newListNode
        if self.head == None:
            self.head = self.tail
        self.listSize += 1

    def remove(self, index: int) -> bool:
        if index + 1 > self.listSize:
            return False

        self.listSize -= 1

        currentNode = self.head
        currentIndex = 0
        while currentIndex < index - 1:
            currentNode = currentNode.next
            currentIndex += 1

        if index == 0 and self.listSize == 0:
            self.head = self.tail = None
            return True

        if index == 0:
            self.head = self.head.next
            return True

        if currentNode.next != None:
            currentNode.next = currentNode.next.next
            if currentNode.next == None:
                self.tail = currentNode

        return True

    def getValues(self) -> list[int]:
        allValues = []
        currentNode = self.head
        while currentNode != None:
            allValues.append(currentNode.value)
            currentNode = currentNode.next
        return allValues