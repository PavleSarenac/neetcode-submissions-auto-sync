class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        characterCounters = dict()
        for character in s:
            if character not in characterCounters.keys():
                characterCounters[character] = 1
            else:
                characterCounters[character] += 1
        for character in t:
            if character not in characterCounters.keys():
                return False
            characterCounters[character] -= 1
        for counter in characterCounters.values():
            if counter != 0:
                return False
        return True