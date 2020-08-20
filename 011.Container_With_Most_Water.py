# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.
# Note: You may not slant the container and n is at least 2.


class Solution:
    def maxArea(self, ls):
        max_area = 0
        s_idx = 0
        e_idx = len(ls) - 1

        while s_idx < e_idx:
            width = e_idx - s_idx
            height = ls[s_idx] if ls[s_idx] < ls[e_idx] else ls[e_idx]
            area = width * height
            max_area = area if area > max_area else max_area
            if ls[s_idx] < ls[e_idx]:
                s_idx += 1
            else:
                e_idx -= 1

        return max_area


sol = Solution()
print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(sol.maxArea([1, 2, 4, 3]))