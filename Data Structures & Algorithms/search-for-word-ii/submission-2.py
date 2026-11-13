class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isWord = False

class Trie:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.addWords(words)

        
    def addWords(self, words: List[str]):
        for word in words:
            self.addWord(word)


    def addWord(self, word: str):
        currentNode = self.root
        for character in word:
            if character not in currentNode.children:
                currentNode.children[character] = TrieNode()
            currentNode = currentNode.children[character]
        currentNode.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie(words)
        numberOfRows = len(board)
        numberOfColumns = len(board[0])
        visited = set()
        foundWords = set()

        def dfs(trieNode: TrieNode, currentWord: str, currentRow: int, currentColumn: int):
            if trieNode.isWord:
                foundWords.add(currentWord)
            
            leftRow, leftColumn = currentRow, currentColumn - 1
            upRow, upColumn = currentRow - 1, currentColumn
            rightRow, rightColumn = currentRow, currentColumn + 1
            downRow, downColumn = currentRow + 1, currentColumn
            nextCells = [
                [leftRow, leftColumn], 
                [upRow, upColumn],
                [rightRow, rightColumn],
                [downRow, downColumn]
            ]

            for nextCell in nextCells:
                nextRow = nextCell[0]
                nextColumn = nextCell[1]

                if ((not 0 <= nextRow < numberOfRows) or 
                    (not 0 <= nextColumn < numberOfColumns) or
                    ((nextRow, nextColumn) in visited) or
                    (not board[nextRow][nextColumn] in trieNode.children)):
                    continue

                nextCharacter = board[nextRow][nextColumn]
                nextTrieNode = trieNode.children[nextCharacter]
                nextWord = currentWord + nextCharacter

                visited.add((currentRow, currentColumn))
                dfs(nextTrieNode, nextWord, nextRow, nextColumn)
                visited.remove((currentRow, currentColumn))

        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] in trie.root.children:
                    dfs(trie.root.children[board[row][column]], board[row][column], row, column)

        return list(foundWords)

        