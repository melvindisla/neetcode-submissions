class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):

            for j in range(1, len(nums)):
                
                if i != j:
                    result = nums[i] + nums[j]

                    if target == result:
                        return [i, j]
                    else:
                        continue
                