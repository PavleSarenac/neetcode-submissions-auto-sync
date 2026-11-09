class PrefixTreeNode:

    def __init__(self):
        self.children = dict()
        self.isWordEnd = False

class PrefixTree:

    def __init__(self):
        self.root = PrefixTreeNode()

    def insert(self, word: str) -> None:
        currentNode = self.root
        for character in word:
            if character not in currentNode.children.keys():
                currentNode.children[character] = PrefixTreeNode()
            currentNode = currentNode.children[character]
        currentNode.isWordEnd = True

    def search(self, word: str) -> bool:
        currentNode = self.root
        for character in word:
            if character not in currentNode.children.keys():
                return False
            currentNode = currentNode.children[character]
        return currentNode.isWordEnd

    def startsWith(self, prefix: str) -> bool:
        currentNode = self.root
        for character in prefix:
            if character not in currentNode.children.keys():
                return False
            currentNode = currentNode.children[character]
        return True