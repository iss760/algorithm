# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# For example, given n = 3, a solution set is:
#   [
#       "((()))",
#       "(()())",
#       "(())()",
#       "()(())",
#       "()()()"
#   ]


class Solution:
    def generateParenthesis(self, n):
        res = []
        s = [("(", 1, 0)]
        while s:
            x, l, r = s.pop()
            if l < r or n < l or n < r:
                continue
            if l == n and r == n:
                res.append(x)
            s.append((x+"(", l+1, r))
            s.append((x+")", l, r+1))
        return res


sol = Solution()
print(sol.generateParenthesis(3))
