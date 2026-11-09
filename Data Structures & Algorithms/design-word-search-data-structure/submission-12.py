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
        def partialSearch(currentNode: TrieNode, wordStartIndex: int) -> bool:
            for wordIndex in range(wordStartIndex, len(word)):
                if word[wordIndex] == '.':
                    for character in currentNode.children.keys():
                        # Improvement of my initial solution -> passing the start index instead of a copy of a substring.
                        if partialSearch(currentNode.children[character], wordIndex + 1):
                            return True
                    return False
                if word[wordIndex] not in currentNode.children.keys():
                    return False
                currentNode = currentNode.children[word[wordIndex]]
            return currentNode.isWordEnd
        return partialSearch(self.root, 0)