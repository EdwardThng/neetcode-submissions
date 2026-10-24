class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {"]": "[", "}": "{", ")": "("}

        for i in s:
            if i in hashmap:
                popped = stack.pop() if stack else "#"
                if hashmap[i] != popped:
                    return False
            else:
                stack.append(i)
        return len(stack) == 0