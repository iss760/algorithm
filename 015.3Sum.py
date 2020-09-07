# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
# Note: The solution set must not contain duplicate triplets.
# Example:
#   Given array nums = [-1, 0, 1, 2, -1, -4],
#   A solution set is:
#   [
#       [-1, 0, 1],
#       [-1, -1, 2]
#   ]


class Solution:
    def threeSum(self, nums):
        """
        :param nums: list[int]
        :return: list[[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums)):
            # 중복되는 원소에 대한 불필요한 계산 생략
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = nums[i]*-1
            s_idx, e_idx = i+1, len(nums)-1
            while s_idx < e_idx:
                if nums[s_idx] + nums[e_idx] == target:
                    res.append([nums[i], nums[s_idx], nums[e_idx]])
                    s_idx += 1
                    while s_idx < e_idx and nums[s_idx] == nums[s_idx-1]:
                        s_idx += 1
                elif nums[s_idx] + nums[e_idx] < target:
                    s_idx += 1
                else:
                    e_idx -= 1
        return res


sol = Solution()
print(sol.threeSum([0, 0, 0]))
print(sol.threeSum([2, -1, -1, 1, 4, 0]))
