class Solution:
    def isValid(self, s: str) -> bool:
        
        cmap = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        stack = []
        
        for char in s:
            if char not in cmap: # if the char is a opener
                stack.append(char)
            elif stack and stack[-1] == cmap[char]: # check if the stack isnt empty and that the top opener is a match
                stack.pop()
            elif char in cmap:
                return False
        return not stack