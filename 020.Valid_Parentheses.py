# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# An input string is valid if:
#   Open brackets must be closed by the same type of brackets.
#   Open brackets must be closed in the correct order.
# Example 1:
#   Input: s = "()"
#   Output: true
# Example 2:
#   Input: s = "()[]{}"
#   Output: true
# Example 3:
#   Input: s = "(]"
#   Output: false


class Solution:
    def isValid(self, s):
        """
        :param s: str 
        :return: bool
        """
        stack = []
        for brk in s:
            if not stack:
                stack.append(brk)
            elif brk in ['(', '{', '[']:
                stack.append(brk)
            else:
                temp = stack.pop()
                if temp not in ['(', '{', '[']:
                    return False
                dic = {'(': ')', '{': '}', '[': ']'}
                if dic[temp] != brk:
                    return False
        if stack:
            return False

        return True


sol = Solution()
print(sol.isValid('[{}]'))
print(sol.isValid('(]'))
print(sol.isValid('[(])'))
print(sol.isValid('[{()()}]'))
print(sol.isValid('))'))

