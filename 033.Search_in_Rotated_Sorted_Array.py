# You are given an integer array nums sorted in ascending order, and an integer target.
# Suppose that nums is rotated at some pivot unknown to you beforehand
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# If target is found in the array return its index, otherwise, return -1.

# Example 1:
#   Input: nums = [4,5,6,7,0,1,2], target = 0
#   Output: 4
# Example 2:
#   Input: nums = [4,5,6,7,0,1,2], target = 3
#   Output: -1
# Example 3:
#   Input: nums = [1], target = 0
#   Output: -1


class Solution:
    def search(self, nums: list, target: int) -> int:
        """
        :param nums:
        :param target:
        :return:
        """
        if target in nums:
            return nums.index(target)
        else:
            return -1


sol = Solution()
print(sol.search([4, 5, 6, 7, 0, 1, 2], 0))
print(sol.search([4, 5, 6, 7, 0, 1, 2], 3))
