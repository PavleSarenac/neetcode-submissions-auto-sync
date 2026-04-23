class HashTableEntry:

    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.currentSize = 0
        self.hashTableEntries = [None] * capacity

    def insert(self, key: int, value: int) -> None:
        keyHash = self.calculateHash(key)

        if self.hashTableEntries[keyHash] is not None and self.hashTableEntries[keyHash].key == key:
            self.hashTableEntries[keyHash].value = value
            return

        if self.hashTableEntries[keyHash] is None:
            self.hashTableEntries[keyHash] = HashTableEntry(key, value)
        else:
            currentKeyHash = keyHash
            while self.hashTableEntries[currentKeyHash] is not None:
                currentKeyHash = (currentKeyHash + 1) % self.capacity
            self.hashTableEntries[currentKeyHash] = HashTableEntry(key, value)

        self.currentSize += 1
        if self.currentSize >= self.capacity / 2:
            self.resize()

    def get(self, key: int) -> int:
        currentKeyHash = self.calculateHash(key)
        while self.hashTableEntries[currentKeyHash]:
            if self.hashTableEntries[currentKeyHash].key == key:
                return self.hashTableEntries[currentKeyHash].value
            currentKeyHash = (currentKeyHash + 1) % self.capacity
        return -1

    def remove(self, key: int) -> bool:
        currentKeyHash = self.calculateHash(key)
        while self.hashTableEntries[currentKeyHash]:
            if self.hashTableEntries[currentKeyHash].key == key:
                self.hashTableEntries[currentKeyHash] = None
                self.currentSize -= 1
                return True
            currentKeyHash = (currentKeyHash + 1) % self.capacity
        return False

    def getSize(self) -> int:
        return self.currentSize

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.currentSize = 0
        self.capacity *= 2
        oldHashTableEntries = self.hashTableEntries
        newHashTableEntries = [None] * self.capacity
        self.hashTableEntries = newHashTableEntries
        for entry in oldHashTableEntries:
            if entry:
                self.insert(entry.key, entry.value)

    def calculateHash(self, key: int) -> int:
        return key % self.capacity