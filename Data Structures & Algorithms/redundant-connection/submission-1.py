class UnionFind:

    def __init__(self, totalNumberOfGraphNodes: int):
        self.nodeToParentMap = dict()
        self.nodeToSubTreeSizeMap = dict()

        for node in range(1, totalNumberOfGraphNodes + 1):
            self.nodeToParentMap[node] = node
            self.nodeToSubTreeSizeMap[node] = 1

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

        if self.nodeToSubTreeSizeMap[root1] > self.nodeToSubTreeSizeMap[root2]:
            self.nodeToParentMap[root2] = root1
            self.nodeToSubTreeSizeMap[root1] += self.nodeToSubTreeSizeMap[root2]
        else:
            self.nodeToParentMap[root1] = root2
            self.nodeToSubTreeSizeMap[root2] += self.nodeToSubTreeSizeMap[root1]

        return True


class Solution:

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        totalNumberOfGraphNodes = len(edges)
        unionFind = UnionFind(totalNumberOfGraphNodes)
        for edge in edges:
            if not unionFind.union(edge[0], edge[1]):
                return edge