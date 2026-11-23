class UnionFind:

    def __init__(self, totalNumberOfGraphNodes: int):
        self.nodeToParentMap = dict()
        self.nodeToSubtreeSizeMap = dict()

        for node in range(totalNumberOfGraphNodes):
            self.nodeToParentMap[node] = node
            self.nodeToSubtreeSizeMap[node] = 1

        self.numberOfConnectedComponents = totalNumberOfGraphNodes

    def find(self, node: int) -> int:
        currentNode = node
        while currentNode != self.nodeToParentMap[currentNode]:
            currentParentNode = self.nodeToParentMap[currentNode]
            currentGrandparentNode = self.nodeToParentMap[currentParentNode]

            self.nodeToParentMap[currentNode] = currentGrandparentNode
            currentNode = currentParentNode
        return currentNode

    def union(self, node1: int, node2: int) -> bool:
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 == root2:
            return False

        if self.nodeToSubtreeSizeMap[root1] > self.nodeToSubtreeSizeMap[root2]:
            self.nodeToParentMap[root2] = root1
            self.nodeToSubtreeSizeMap[root1] += self.nodeToSubtreeSizeMap[root2]
        else:
            self.nodeToParentMap[root1] = root2
            self.nodeToSubtreeSizeMap[root2] += self.nodeToSubtreeSizeMap[root1]

        self.numberOfConnectedComponents -= 1

        return True


class Solution:
    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        unionFind = UnionFind(n)
        for edge in edges:
            unionFind.union(edge[0], edge[1])
        return unionFind.numberOfConnectedComponents