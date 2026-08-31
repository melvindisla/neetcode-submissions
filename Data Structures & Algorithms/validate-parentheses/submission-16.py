class Solution:
    def isValid(self, s: str) -> bool:
        mmap = {
            '}':'{', ')':'(', ']':'['
            }
        
        stack = []
    
        for char in s:
            if char not in mmap:
                stack.append(char)
            elif stack and stack[-1] == mmap[char]:
                stack.pop()
            else:
                return False
        return not stack