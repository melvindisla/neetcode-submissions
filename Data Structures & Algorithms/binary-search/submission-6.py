class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            pivot = (hi + lo) // 2

            # if the element is equal to the target
            if nums[pivot] == target:
                return pivot
            
            # if the element is greater than the target, set high to pivot - 1
            elif nums[pivot] > target:
                hi = pivot - 1
            elif nums[pivot] < target:
                lo = pivot + 1
        return -1