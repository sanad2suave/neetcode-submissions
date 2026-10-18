class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ans = 0
        for i in tokens:
            if i == "+":
                b = stack.pop()
                a = stack.pop()
                ans = a + b
                stack.append(ans)
            elif i == "-":
                b = stack.pop()
                a = stack.pop()
                ans = a - b
                stack.append(ans)
            elif i == "*":
                b = stack.pop()
                a = stack.pop()
                ans = a * b
                stack.append(ans)
            elif i == "/":
                b = stack.pop()
                a = stack.pop()
                ans = int(a / b)
                stack.append(ans)
            else:
                stack.append(int(i))
        return stack.pop()