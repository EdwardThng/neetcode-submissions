class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        i = 0

        if len(tokens) == 1:
            return int(tokens[0])
        
        operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)
        }
        while i < len(tokens):
            if tokens[i] not in operations:
                stack.append(tokens[i])
                i += 1
                continue
            b = int(stack.pop())
            a = int(stack.pop())
            res = operations[tokens[i]](a, b)
            stack.append(res)
            i += 1

        return res
        