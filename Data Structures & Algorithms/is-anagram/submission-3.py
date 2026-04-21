class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashMap = dict()
        for i in range(len(s)):
            if hashMap.get(s[i]):
                hashMap[s[i]] += 1
            else:
                hashMap[s[i]] = 1
            
            if hashMap.get(t[i]):
                hashMap[t[i]] -= 1
            else:
                hashMap[t[i]] = -1

        for value in hashMap.values():
            if value:
                return False
            
        return True