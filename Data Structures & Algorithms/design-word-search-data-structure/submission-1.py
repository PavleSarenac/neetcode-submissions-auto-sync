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
        currentNode = self.root
        for wordIndex in range(len(word)):
            if word[wordIndex] != '.' and word[wordIndex] not in currentNode.children.keys():
                return False
            if word[wordIndex] == '.':
                searchResult = False
                for character in currentNode.children.keys():
                    wordWithRemovedDot = word[0:wordIndex] + character + word[wordIndex + 1:len(word)]
                    searchResult = searchResult or self.search(wordWithRemovedDot)
                return searchResult
            else:
                currentNode = currentNode.children[word[wordIndex]]
        return currentNode.isWordEnd
