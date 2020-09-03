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
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = nums[i] * -1
            s_idx, e_idx = i + 1, len(nums) - 1
            while s_idx < e_idx:
                if nums[s_idx] + nums[e_idx] == target:
                    res.append([nums[i], nums[s_idx], nums[e_idx]])
                    s_idx += 1
                    while s_idx < e_idx and nums[s_idx] == nums[s_idx - 1]:
                        s_idx += 1
                elif nums[s_idx] + nums[e_idx] < target:
                    s_idx += 1
                else:
                    e_idx -= 1
        return res



sol = Solution()
print(sol.threeSumClosest([-1, 2, 1, -4], 2))
