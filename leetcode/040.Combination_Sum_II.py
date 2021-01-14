# Given a collection of candidate numbers (candidates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.

# Example 1:
#   Input: candidates = [10,1,2,7,6,1,5], target = 8
#   Output:
#       [
#       [1,1,6],
#       [1,2,5],
#       [1,7],
#       [2,6]
#       ]


class Solution:
    def combinationSum2(self, candidates, target):
        ret = []
        self.dfs(sorted(candidates), target, 0, [], ret)
        return ret

    def dfs(self, nums, target, idx, path, ret):
        if target < 0:
            return
        elif target == 0:
            return ret.append(path)
        else:
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                self.dfs(nums, target-nums[i], i+1, path+[nums[i]], ret)


sol = Solution()
print(sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))

