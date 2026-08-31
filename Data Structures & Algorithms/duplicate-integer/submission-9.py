class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        map_table = {}

        for num in nums:
            if num not in map_table:
                map_table[num] = 1
            else:
                return True
        return False