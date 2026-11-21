class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for word in strs:
            wordLength = str(len(word))
            endOfWordLengthDelimiter = "#"
            encodedString += wordLength + endOfWordLengthDelimiter + word
        return encodedString

    def decode(self, s: str) -> List[str]:
        decodedStrings = []
        currentCharacterIndex = 0
        endOfWordLengthDelimiter = "#"
        print(s)
        while currentCharacterIndex < len(s):
            currentStringLength = ""
            while s[currentCharacterIndex] != endOfWordLengthDelimiter:
                currentStringLength += s[currentCharacterIndex]
                currentCharacterIndex += 1
            currentCharacterIndex += 1
            currentStringLength = int(currentStringLength)

            currentString = s[currentCharacterIndex:currentCharacterIndex + currentStringLength]
            decodedStrings.append(currentString)

            currentCharacterIndex += currentStringLength
        return decodedStrings