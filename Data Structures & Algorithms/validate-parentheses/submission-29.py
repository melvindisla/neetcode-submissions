class Solution:
    def isValid(self, s: str) -> bool:
        
        cmap = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        stack = []
        
        for char in s:
            if char not in cmap: # if the character is a opening bracket
                stack.append(char)
            elif stack and stack[-1] == cmap[char]: # if the stack is not empty and the top bracket is a match
                stack.pop()
            # elif char in cmap: # the 
            else:
                return False
        return not stack