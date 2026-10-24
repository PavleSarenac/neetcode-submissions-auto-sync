class Solution:
    def isPalindrome(self, s: str) -> bool:
        leftPointer, rightPointer = 0, len(s) - 1

        def isAlphanumericCharacter(character: str) -> bool:
            characterAsciiCode = ord(character)
            return (ord('a') <= characterAsciiCode <= ord('z') or 
                    ord('A') <= characterAsciiCode <= ord('Z') or
                    ord('0') <= characterAsciiCode <= ord('9'))

        def isUppercaseCharacter(character: str) -> bool:
            characterAsciiCode = ord(character)
            return ord('A') <= characterAsciiCode <= ord('Z')

        while leftPointer < rightPointer:
            leftCharacter = s[leftPointer]
            rightCharacter = s[rightPointer]

            if not isAlphanumericCharacter(leftCharacter):
                leftPointer += 1
                continue

            if not isAlphanumericCharacter(rightCharacter):
                rightPointer -= 1
                continue

            if isUppercaseCharacter(leftCharacter):
                leftCharacter = chr(ord('a') + (ord(leftCharacter) - ord('A')))
            if isUppercaseCharacter(rightCharacter):
                rightCharacter = chr(ord('a') + (ord(rightCharacter) - ord('A')))

            if leftCharacter != rightCharacter:
                return False

            leftPointer += 1
            rightPointer -= 1

        return True