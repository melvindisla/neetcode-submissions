class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # step 1: create instance of a map
        # step 2: loop through the list
        # step 3: if the value is in the map, then return true
        # step 4: add value to the hashmap
        # step 5: return false

        hashmap = {}

        for  i, num in enumerate(nums):
            if num in hashmap:
                return True
            hashmap[num] = i
        return False