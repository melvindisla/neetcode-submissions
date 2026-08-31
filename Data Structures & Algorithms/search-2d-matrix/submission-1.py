class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for nums in matrix:

            lo, hi = 0, len(nums)-1

            while lo <= hi:

                mid = lo + (hi - lo) // 2

                if nums[mid] > target:
                    hi = mid - 1
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    return True
        return False