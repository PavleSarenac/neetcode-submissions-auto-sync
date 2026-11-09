class TrieNode:

    def __init__(self):
        self.children = dict()
        self.isWordEnd = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        currentNode = self.root
        for character in word:
            if character not in currentNode.children.keys():
                currentNode.children[character] = TrieNode()
            currentNode = currentNode.children[character]
        currentNode.isWordEnd = True

    def search(self, word: str) -> bool:
        def partialSearch(currentNode: TrieNode, word: str) -> bool:
            for wordIndex in range(len(word)):
                if word[wordIndex] == '.':
                    for character in currentNode.children.keys():
                        if partialSearch(currentNode.children[character], word[wordIndex + 1:len(word)]):
                            return True
                    return False
                if word[wordIndex] not in currentNode.children.keys():
                    return False
                currentNode = currentNode.children[word[wordIndex]]
            return currentNode.isWordEnd
        return partialSearch(self.root, word)
