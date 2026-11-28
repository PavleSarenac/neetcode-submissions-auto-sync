class UnionFind:
    def __init__(self, treeSize: int):
        self.nodeToParentMap = dict()
        self.nodeToSubTreeSizeMap = dict()

        for node in range(treeSize):
            self.nodeToParentMap[node] = node
            self.nodeToSubTreeSizeMap[node] = 1

        if treeSize > 0:
            self.longestConsecutiveSequence = 1
        else:
            self.longestConsecutiveSequence = 0

    def find(self, node: int) -> int:
        currentNode = node
        while currentNode != self.nodeToParentMap[currentNode]:
            currentNodeParent = self.nodeToParentMap[currentNode]
            currentNodeGrandparent = self.nodeToParentMap[currentNodeParent]

            self.nodeToParentMap[currentNode] = currentNodeGrandparent
            currentNode = currentNodeParent
        return currentNode

    def union(self, node1: int, node2: int) -> bool:
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 == root2:
            return False

        if self.nodeToSubTreeSizeMap[root1] > self.nodeToSubTreeSizeMap[root2]:
            self.nodeToParentMap[root2] = root1
            self.nodeToSubTreeSizeMap[root1] += self.nodeToSubTreeSizeMap[root2]
            self.longestConsecutiveSequence = max(self.longestConsecutiveSequence, self.nodeToSubTreeSizeMap[root1])
        else:
            self.nodeToParentMap[root1] = root2
            self.nodeToSubTreeSizeMap[root2] += self.nodeToSubTreeSizeMap[root1]
            self.longestConsecutiveSequence = max(self.longestConsecutiveSequence, self.nodeToSubTreeSizeMap[root2])

        return True 


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unionFind = UnionFind(len(nums))
        numberToIndexMap = dict()
        for numberIndex in range(len(nums)):
            if nums[numberIndex] in numberToIndexMap:
                continue

            numberToIndexMap[nums[numberIndex]] = numberIndex

            previousSequenceNumber = nums[numberIndex] - 1
            if previousSequenceNumber in numberToIndexMap:
                unionFind.union(numberIndex, numberToIndexMap[previousSequenceNumber])

            nextSequenceNumber = nums[numberIndex] + 1
            if nextSequenceNumber in numberToIndexMap:
                unionFind.union(numberIndex, numberToIndexMap[nextSequenceNumber])

        return unionFind.longestConsecutiveSequence