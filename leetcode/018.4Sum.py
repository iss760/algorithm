# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums
# such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
# Note: The solution set must not contain duplicate quadruplets.
# Example:
#   Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
#   A solution set is:
#   [
#     [-1,  0, 0, 1],
#     [-2, -1, 1, 2],
#     [-2,  0, 0, 2]
#   ]


class Solution:
    def fourSum(self, nums, target):
        """
        :param nums: list[int]
        :param target: int
        :return: list[[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if nums[j] == nums[j - 1] and j-1 != i:
                    continue

                tar = target - nums[i] - nums[j]
                s_idx, e_idx = j+1, len(nums)-1
                while s_idx < e_idx:
                    if nums[s_idx] + nums[e_idx] == tar:
                        res.append([nums[i], nums[j], nums[s_idx], nums[e_idx]])
                        s_idx += 1
                        while s_idx < e_idx and nums[s_idx] == nums[s_idx-1]:
                            s_idx += 1
                    elif nums[s_idx] + nums[e_idx] < tar:
                        s_idx += 1
                    else:
                        e_idx -= 1
        return res


sol = Solution()
print(sol.fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0))
print(sol.fourSum([1, 0, -1, 0, -2, 2], 3))
