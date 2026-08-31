class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        elements = []
        operators = {"+", "-", "*", "/"}
        for i in tokens:
            if i not in operators:
                elements.append(int(i))
            else:
                num1 = elements[-1]
                elements.pop()
                num2 = elements[-1]
                elements.pop()
                if i == "+":
                    total = num2 + num1
                elif i == "-":
                    total = num2 - num1
                elif i == "*":
                    total = num2 * num1
                elif i == "/": 
                    total = int(num2 / num1)
                elements.append(total)
        return elements[-1]