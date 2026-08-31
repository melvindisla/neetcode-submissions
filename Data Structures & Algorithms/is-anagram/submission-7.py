class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        if len(s) != len(t):
            return False
    
        char_map = {}
        
        for char_s, char_t in zip(s, t):
            
            if char_s not in char_map:
                char_map[char_s] = 1
            else:
                char_map[char_s] += 1
            
            if char_t not in char_map:
                char_map[char_t] = -1
            else:
                char_map[char_t] -= 1
        
        return all(not vals for vals in char_map.values())