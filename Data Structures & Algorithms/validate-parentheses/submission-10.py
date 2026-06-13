class Solution:
    def isValid(self, s: str) -> bool:
        seen = {')':'(', '}':'{',']':'['}
        stack = []
        for i in s:
            if i in seen:
                if not stack or stack.pop() != seen[i]:
                    return False
            else:
                stack.append(i)
        if stack:
            return False
        return True
        