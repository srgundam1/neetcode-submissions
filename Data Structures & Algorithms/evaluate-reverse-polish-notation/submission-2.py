class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # if number, push on stack
        # if operand, pop two elements (numbers)
        # push answer to stack

        stack = []

        for i in tokens:
            if i == '+':
                a,b = stack.pop(),stack.pop()
                stack.append(a+b)
            elif i == '-':
                a,b = stack.pop(),stack.pop()
                stack.append(b-a)
            elif i == '*':
                a,b = stack.pop(),stack.pop()
                stack.append(a*b)
            elif i == '/':
                a,b = stack.pop(),stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(i))
        return stack.pop()

        