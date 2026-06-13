class Solution:
    def isValid(self, s: str) -> bool:
        seen = {')':'(', '}':'{',']':'['}
        stack = []
        for i in s:
            if i not in seen:
                stack.append(i)
            else:
                if not stack or stack.pop() != seen[i]:
                    return False
        if stack:
            return False
        return True
        