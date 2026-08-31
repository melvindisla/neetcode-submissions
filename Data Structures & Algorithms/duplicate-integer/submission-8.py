class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # Step 1: initialize the map
        # Step 2: loop through the loop
        # Step 3: if the value is not in the map
        # Step 4: add the value to the map
        # Step 5: else
        # Step 6: Return True

        mmap = {}
        for num in nums:
            if num not in mmap:
                mmap[num] = 1
            else:
                return True
        return False