class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for word in strs:
            wordLengthString = str(len(word) // 100) + str((len(word) // 10) % 10) + str(len(word) % 10)
            encodedString += wordLengthString + word
        return encodedString

    def decode(self, s: str) -> List[str]:
        decodedStrings = []
        currentCharacterIndex = 0
        print(s)
        while currentCharacterIndex < len(s):
            currentStringLength = int(s[currentCharacterIndex:currentCharacterIndex + 3])
            print(currentStringLength)
            currentString = ""
            currentCharacterIndex += 3
            for currentCharacterIndex in range(currentCharacterIndex, currentCharacterIndex + currentStringLength):
                currentString += s[currentCharacterIndex]
            if currentStringLength > 0:
                currentCharacterIndex += 1
            decodedStrings.append(currentString)
        return decodedStrings
