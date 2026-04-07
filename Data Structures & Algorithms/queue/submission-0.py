class ListNode:
    def __init__(self, value, previous = None, next = None):
        self.value = value
        self.previous = previous
        self.next = next

class Deque:
    
    def __init__(self):
        self.head = ListNode("#")
        self.tail = ListNode("#")
        self.head.next = self.tail
        self.tail.previous = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        newNode = ListNode(value, self.tail.previous, self.tail)
        self.tail.previous.next = newNode
        self.tail.previous = newNode

    def appendleft(self, value: int) -> None:
        newNode = ListNode(value, self.head, self.head.next)
        self.head.next.previous = newNode
        self.head.next = newNode

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        value = self.tail.previous.value
        self.tail.previous.previous.next = self.tail
        self.tail.previous = self.tail.previous.previous
        return value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        value = self.head.next.value
        self.head.next.next.previous = self.head
        self.head.next = self.head.next.next
        return value