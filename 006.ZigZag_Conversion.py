#   The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
#   (you may want to display this pattern in a fixed font for better legibility)
#   P   A   H   N
#   A P L S I I G
#   Y   I   R
#   And then read line by line: "PAHNAPLSIIGYIR"
#   Write the code that will take a string and make this conversion given a number of rows:
#   string convert(string s, int numRows);
#   Example 1:
#       Input: s = "PAYPALISHIRING", numRows = 3
#       Output: "PAHNAPLSIIGYIR"
#   Example 2:
#       Input: s = "PAYPALISHIRING", numRows = 4
#       Output: "PINALSIGYAHRPI"
#   Explanation:
#       P     I    N
#       A   L S  I G
#       Y A   H R
#       P     I

class Solution:
    def convert(self, s, numRows):
        """
        :param s: str
        :param numRows: int
        :return: str
        """
        max_idx = len(s) - 1
        # 세로, 가로가 한줄로 배열되는 경우
        if len(s) <= numRows or numRows == 1:
            return s

        res = ""
        for row in range(numRows):
            # 규칙성
            jump1 = (numRows - row - 1) * 2
            jump2 = row * 2

            cur = row
            res += s[cur]
            while True:
                if cur+jump1 > max_idx:
                    break
                cur += jump1
                if jump1 != 0 and cur <= max_idx:
                    res += s[cur]

                if cur+jump2 > max_idx:
                    break
                cur += jump2
                if jump2 != 0 and cur <= max_idx:
                    res += s[cur]

        return res

sol = Solution()
print(sol.convert("PAYPALISHIRING", 4))
print(sol.convert("ABCDE", 4))
print(sol.convert("ABC", 2))
print(sol.convert("PAYPALISHIRINGTA", 4))
print(sol.convert("PAYPALISHIRING", 5))

