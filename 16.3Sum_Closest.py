# Given an array nums of n integers and an integer target,
# find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers. You may assume that each input would have exactly one solution.
# Example 1:
#   Input: nums = [-1,2,1,-4], target = 1
#   Output: 2
#   Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :param nums: list[int]
        :param target: int
        :return: int
        """
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    return sum

                if abs(sum - target) < abs(res - target):
                    res = sum

                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1

        return res



sol = Solution()
print(sol.threeSumClosest([-1, 2, 1, -4], 1))
