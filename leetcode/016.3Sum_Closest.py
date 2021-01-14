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
            s_idx, e_idx = i + 1, len(nums) - 1
            while s_idx < e_idx:
                sum = nums[i] + nums[s_idx] + nums[e_idx]
                if sum == target:
                    return sum
                # 근접 값 확인
                if abs(sum - target) < abs(res - target):
                    res = sum

                if sum < target:
                    s_idx += 1
                elif sum > target:
                    e_idx -= 1

        return res



sol = Solution()
print(sol.threeSumClosest([-1, 2, 1, -4], 1))
