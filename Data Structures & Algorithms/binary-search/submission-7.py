class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # we define the high and lo of the array, this is crucial for determining the pivot index
        lo, hi = 0, len(nums)-1

        # while lo is less than or equal to high
        while lo <= hi:

            # determine the pivot index first
            pivot = (hi + lo) // 2

            # if the element is greater than the target, redefine hi value
            if nums[pivot] > target:
                hi = pivot - 1

            # else if elenent is lesser than the target, redefine lo value
            elif nums[pivot] < target:
                lo = pivot + 1
            
            # return the pivot index
            else:
                return pivot
        # the element is not in the list
        return -1