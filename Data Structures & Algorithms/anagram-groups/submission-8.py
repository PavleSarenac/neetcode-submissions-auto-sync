class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedAnagrams = dict()
        for word in strs:
            anagramCharacterCount = [0] * 26
            for character in word:
                characterIndex = ord(character) - ord('a')
                anagramCharacterCount[characterIndex] += 1
            # anagramCharacterCount list needs to be converted into an immutable data structure
            # in order for it to be a valid dictionary key in Python. Lists can't be dictionary
            # keys in Python because since they are mutable and therefore not hashable.
            anagramCharacterCount = tuple(anagramCharacterCount)
            if anagramCharacterCount not in groupedAnagrams:
                groupedAnagrams[anagramCharacterCount] = [word]
            else:
                groupedAnagrams[anagramCharacterCount].append(word)
        return list(groupedAnagrams.values())
