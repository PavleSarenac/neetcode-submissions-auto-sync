class UnionFind:

    def __init__(self, totalNumberOfGraphNodes: int):
        self.nodeToParentMap = dict()
        self.nodeToSubTreeSizeMap = dict()

        for node in range(totalNumberOfGraphNodes):
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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        unionFind = UnionFind(len(accounts))
        emailToAccountIndexMap = dict()
        for accountIndex in range(len(accounts)):
            for emailIndex in range(1, len(accounts[accountIndex])):
                email = accounts[accountIndex][emailIndex]
                if email not in emailToAccountIndexMap:
                    emailToAccountIndexMap[email] = accountIndex
                else:
                    unionFind.union(emailToAccountIndexMap[email], accountIndex)
        
        groupRootAccountIndexToEmailsMap = dict()
        for accountIndex in range(len(accounts)):
            groupRootAccountIndex = unionFind.find(accountIndex)
            if groupRootAccountIndex not in groupRootAccountIndexToEmailsMap:
                groupRootAccountIndexToEmailsMap[groupRootAccountIndex] = set()
            for emailIndex in range(1, len(accounts[accountIndex])):
                email = accounts[accountIndex][emailIndex]
                groupRootAccountIndexToEmailsMap[groupRootAccountIndex].add(email)

        mergedAccounts = []
        for groupRootAccountIndex, emails in groupRootAccountIndexToEmailsMap.items():
            accountName = accounts[groupRootAccountIndex][0]
            sortedEmails = sorted(emails)
            mergedAccounts.append([accountName] + sortedEmails)
        
        return mergedAccounts

