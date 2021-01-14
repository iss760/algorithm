# Given a sorted array and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array.

# Example 1:
#   Input: [1,3,5,6], 5
#   Output: 2


class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        l, r = 0, len(nums)-1
        if nums[0] >= target:
            return 0
        elif nums[-1] < target:
            return len(nums)

        while True:
            mid = (r+l)//2
            if r-l <= 1:
                return r
            elif nums[mid] < target:
                l = mid
            else:
                r = mid
