# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such arrangement is not possible,
# it must rearrange it as the lowest possible order (ie, sorted in ascending order).
# The replacement must be in-place and use only constant extra memory.

# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
#   1,2,3 → 1,3,2
#   3,2,1 → 1,2,3
#   1,1,5 → 1,5,1


class Solution:
    def nextPermutation(self, nums):
        """
        :param nums: list[int]
        :return: None
        """
        # 시작점 설정 (ex. 3 2 5 6 4 3 1(i,j))
        i = j = len(nums)-1

        # 내림차순이 끝나는 곳까지 i 이동 (ex. 3 2 5(i) 6 4 3 1(j))
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1

        # nums가 내림차순 정렬일 경우
        if i == 0:
            nums.reverse()
            return

        k = i - 1   # swap 위치 설정 (ex. 3 2(k) 5(i) 6 4 3 1(j))

        # swap 위치 설정 (ex. 3 2(k) 5(i) 6 4 3(j) 1)
        while nums[j] <= nums[k]:
            j -= 1

        nums[k], nums[j] = nums[j], nums[k]     # swap (ex. 3 3(k) 5(i) 6 4 2(j) 1)

        l, r = k+1, len(nums)-1  # 뒤집을 부분 위치 설정 (ex. 3 3(k) 5(i,l) 6 4 2(j) 1(r))

        # 나머지 부분 뒤집기 (ex. 3 3 5 1 2 4 6 5)
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


sol = Solution()
print(sol.nextPermutation([1, 2, 3]))
print(sol.nextPermutation([2, 3, 4, 1]))
print(sol.nextPermutation([3, 2, 1, 5]))
print(sol.nextPermutation([1, 3, 2]))
