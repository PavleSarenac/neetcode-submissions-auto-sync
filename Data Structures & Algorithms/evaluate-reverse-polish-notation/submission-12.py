class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif token == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif token == "-":
                secondOperand = int(stack.pop())
                firstOperand = int(stack.pop())
                stack.append(firstOperand - secondOperand)
            elif token == "/":
                secondOperand = int(stack.pop())
                firstOperand = int(stack.pop())
                result = firstOperand // secondOperand
                if firstOperand % secondOperand != 0 and result < 0:
                    result += 1
                stack.append(result)
            else:
                stack.append(int(token))
        return stack.pop()