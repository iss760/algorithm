# Given a string containing just the characters '(' and ')',
# find the length of the longest valid (well-formed) parentheses substring.

# Example 1:
#   Input: "(()"
#   Output: 2
#   Explanation: The longest valid parentheses substring is "()"
# Example 2:
#   Input: ")()())"
#   Output: 4
#   Explanation: The longest valid parentheses substring is "()()"


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1, ]
        sub_len, res = 0, 0
        for i, brk in enumerate(s):
            if not stack:
                stack.append(i)
            elif brk == ')':
                del stack[-1]
                if not stack:
                    stack.append(i)
                    continue
                temp = stack[-1]
                sub_len = i - temp
            else:
                stack.append(i)

            res = sub_len if sub_len > res else res

        return res


sol = Solution()
print(sol.longestValidParentheses("(()"))
print(sol.longestValidParentheses("()())"))
print(sol.longestValidParentheses("(())(()(("))
print(sol.longestValidParentheses("(())()"))
print(sol.longestValidParentheses(")()())"))
