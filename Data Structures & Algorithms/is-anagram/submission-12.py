class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            
        if len(s) != len(t):
                return False

        mmap = {}

        for char_s, char_t in zip(s, t):
            
            if char_s not in mmap:
                mmap[char_s] = 1
            else:
                mmap[char_s] += 1

            if char_t not in mmap:
                mmap[char_t] = -1
            else:
                mmap[char_t] -= 1

        return all(not val for val in mmap.values())