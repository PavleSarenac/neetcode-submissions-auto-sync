class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []
        for currentCharacter in s:
            if currentCharacter == ')':
                if len(stack) == 0 or stack.pop() != '(':
                    return False
            elif currentCharacter == '}':
                if len(stack) == 0 or stack.pop() != '{':
                    return False
            elif currentCharacter == ']':
                if len(stack) == 0 or stack.pop() != '[':
                    return False
            else:
                stack.append(currentCharacter)
        return len(stack) == 0