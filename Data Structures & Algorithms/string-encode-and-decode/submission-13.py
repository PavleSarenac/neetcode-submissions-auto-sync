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
        while currentCharacterIndex < len(s):
            currentStringLength = int(s[currentCharacterIndex:currentCharacterIndex + 3])
            currentCharacterIndex += 3
            currentString = s[currentCharacterIndex:currentCharacterIndex + currentStringLength]
            decodedStrings.append(currentString)
            currentCharacterIndex += currentStringLength
        return decodedStrings