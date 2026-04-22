class ListNode:
    
    def __init__(self, key: int, value: int, previousNode = None, nextNode = None):
        self.key = key
        self.value = value
        self.previousNode = previousNode
        self.nextNode = nextNode

class DoublyLinkedList:
    
    def __init__(self):
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.nextNode = self.tail
        self.tail.previousNode = self.head

    def popLeft(self, node: ListNode):
        node.previousNode.nextNode = node.nextNode
        node.nextNode.previousNode = node.previousNode

    def pushRight(self, node: ListNode) -> ListNode:
        node.previousNode = self.tail.previousNode
        node.nextNode = self.tail
        self.tail.previousNode.nextNode = node
        self.tail.previousNode = node
        return node

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashMap = dict()
        self.usedKeysHistory = DoublyLinkedList()

    def get(self, key: int) -> int:
        node = self.hashMap.get(key)
        if node:
            self.usedKeysHistory.popLeft(node)
            self.usedKeysHistory.pushRight(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        existingNode = self.hashMap.get(key)
        if existingNode:
            existingNode.value = value
            self.usedKeysHistory.popLeft(existingNode)
            self.usedKeysHistory.pushRight(existingNode)
            return
        
        if len(self.hashMap.keys()) == self.capacity:
            headNode = self.usedKeysHistory.head.nextNode
            self.hashMap.pop(headNode.key)
            self.usedKeysHistory.popLeft(headNode)

        newNode = ListNode(key, value)
        self.usedKeysHistory.pushRight(newNode)
        self.hashMap[key] = newNode