class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(["/", "*", "+", "-"])

        for token in tokens:
            if token in operators:
                operand2 = stack.pop()
                operand1 = stack.pop()
                res = self.operationHelper(operand1, operand2, token)
                stack.append(res)
            else:
                stack.append(int(token))
        return stack[-1]


    def operationHelper(self, operand1, operand2, operator):
        operand1 = int(operand1)
        operand2 = int(operand2)
        if operator == '/':
            return int(float(operand1) / operand2)
        elif operator == '*':
            return operand1 * operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '+':
            return operand1 + operand2
        else:
            pass



        