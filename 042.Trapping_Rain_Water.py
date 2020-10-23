# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it can trap after raining.

# Example 1:
#   Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
#   Output: 6
#   Explanation: The above elevation map (black section) is represented
#                by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case,
#                6 units of rain water (blue section) are being trapped.
# Example 2:
#   Input: height = [4,2,0,3,2,5]
#   Output: 9


class Solution:
    def trap(self, height: list) -> int:
        if not height:
            return 0

        l_idx, r_idx = 0, len(height)-1
        l_max, r_max = height[l_idx], height[r_idx]
        res = 0

        while l_idx < r_idx:
            if height[l_idx] <= height[r_idx]:
                if height[l_idx] < l_max:
                    res = res + (l_max - height[l_idx])
                else:
                    l_max = height[l_idx]
                l_idx += 1
            else:
                if height[r_idx] <= height[r_idx]:
                    if height[r_idx] < r_max:
                        res = res + (r_max - height[r_idx])
                    else:
                        r_max = height[r_idx]
                    r_idx -= 1

        return res


sol = Solution()
print(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(sol.trap([4, 2, 0, 3, 2, 5]))
