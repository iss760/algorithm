#   You are given two non-empty linked lists representing two non-negative integers.
#   The digits are stored in reverse order and each of their nodes contain a single digit.
#   Add the two numbers and return it as a linked list.
#   You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#   Example:
#       Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#       Output: 7 -> 0 -> 8
#       Explanation: 342 + 465 = 807.


# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def __init__(self):
        self.listNode = ListNode()

    def addTwoNumbers(self, l1, l2):
        '''
        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        '''
        num1 = 0
        i = 1
        now_val = l1.val
        next_node = l1.next
        while next_node.next is None:
            num1 += now_val * 1
            now_val = next_node.val
            next_node = next_node.next
            i *= 10

        num2 = 0
        i = 1
        now_val = l2.val
        next_node = l2.next
        while next_node.next is None:
            num2 += now_val * 1
            now_val = next_node.val
            next_node = next_node.next
            i *= 10

        print(num1, num2)


sol = Solution()
print(sol.addTwoNumbers([2, 4, 3], [5, 6, 4]))
