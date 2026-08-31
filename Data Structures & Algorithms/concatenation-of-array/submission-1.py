class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        ans = []

        # this loop is used to go theough the nums array 2 times
        for i in range(2):
            # this for loop is used to copy the values from nums to ans
            for num in nums:
                ans.append(num)
        return ans
