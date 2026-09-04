class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            match i:
                case "+":
                    num2 = int(stack.pop())
                    num1 = int(stack.pop())
                    total = num1 + num2
                    stack.append(total)
                case "-":
                    num2 = int(stack.pop())
                    num1 = int(stack.pop())
                    total = num1 - num2
                    stack.append(total)
                case "*":
                    num2 = int(stack.pop())
                    num1 = int(stack.pop())
                    total = num1 * num2
                    stack.append(total)
                case "/":
                    num2 = int(stack.pop())
                    num1 = int(stack.pop())
                    total = int(num1 / num2)
                    stack.append(total)
                case _:
                    stack.append(int(i))
        print(stack)
        return stack[-1]