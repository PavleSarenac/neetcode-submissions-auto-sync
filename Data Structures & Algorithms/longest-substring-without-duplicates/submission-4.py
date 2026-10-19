class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        leftWindowEdge = rightWindowEdge = 0
        currentSubstring = set()
        for character in s:
            if character in currentSubstring:
                maxLength = max(maxLength, rightWindowEdge - leftWindowEdge)
                while s[leftWindowEdge] != character:
                    currentSubstring.remove(s[leftWindowEdge])
                    leftWindowEdge += 1
                currentSubstring.remove(s[leftWindowEdge])
                leftWindowEdge += 1
            currentSubstring.add(character)
            rightWindowEdge += 1
        maxLength = max(maxLength, rightWindowEdge - leftWindowEdge)
        return maxLength