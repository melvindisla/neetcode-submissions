class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        char_map = {}

        for idx, char in enumerate(s):
            if char not in char_map:
                char_map[char] = 1
            else:
                char_map[char] += 1
                
        for idx, char in enumerate(t):
            if char in char_map:
                char_map[char] -= 1
    
        return all(not vals for vals in char_map.values())