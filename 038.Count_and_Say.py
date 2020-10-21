# The count-and-say sequence is the sequence of integers with the first five terms as following:
#     1. 1
#     2. 11
#     3. 21
#     4. 1211
#     5. 111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
#
# Given an integer n where 1 ≤ n ≤ 30, generate the n(th) term of the count-and-say sequence.
# You can do so recursively, in other words from the previous member read off the digits,
# counting the number of digits in groups of the same digit.
# Note: Each term of the sequence of integers will be represented as a string.


class Solution:
    def countAndSay(self, n: int):
        # 첫째 항일 경우 처리
        if n == 1:
            return '1'

        cas = 1
        for _ in range(n-1):
            cas = str(cas)
            cnt, temp = 0, ''
            for i in range(len(cas)):
                cnt += 1
                if i != len(cas)-1 and cas[i] != cas[i+1]:
                    temp = temp + str(cnt) + str(cas[i])
                    cnt = 0
            temp = temp + str(cnt) + str(cas[-1])       # 마지막 숫자 처리
            cas = temp

        return cas


sol = Solution()
for i in range(1, 21):
    print(sol.countAndSay(i))
