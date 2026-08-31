class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        previous_values = {}

        for i in range(len(nums)):

            diff = target - nums[i]
            if diff in previous_values:
                return [previous_values[diff], i]
            previous_values[nums[i]]=i










        # for i in range(len(nums)):
        #     for j in range(1, len(nums)):
        #         # in the return array we cannot return duplicate indices
        #         if i != j:
        #             result = nums[i] + nums[j]
        #             if target == result:
        #                 return [i, j]
        #             else:
        #                 continue


                