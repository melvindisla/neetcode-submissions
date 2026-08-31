class Solution:
    def isValid(self, s: str) -> bool:
        mmap = {
            '}':'{', ')':'(', ']':'['
            }
        
        stack = []
    
        for char in s:

            if char in mmap and len(stack) == 0:
                return False
            elif char not in mmap:
                stack.append(char)
            elif char in mmap and stack[-1] == mmap[char]:
                stack.pop()
            else:
                return False
        return not stack