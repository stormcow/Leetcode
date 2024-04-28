class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_p = {"(": ")", "[": "]", "{": "}"}
        for parentheses in s:
            if valid_p.get(parentheses, -1) != -1:
                stack.append(parentheses)
            elif stack:
                from_stack = stack.pop()
                if valid_p[from_stack] != parentheses:
                    return False
            else:
                return False
        return not stack
