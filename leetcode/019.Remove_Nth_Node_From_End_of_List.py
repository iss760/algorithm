# Given a linked list, remove the n-th node from the end of list and return its head.
# Example:
#   Given linked list: 1->2->3->4->5, and n = 2.
#   After removing the second node from the end, the linked list becomes 1->2->3->5.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node = head
        cnt = 0
        while node is not None:
            node = node.next
            cnt += 1

        node = head
        for _ in range(cnt - n - 1):
            node = node.next

        if n == 1:
            if cnt == 1:
                head = None
            else:
                node.next = None
        elif n == cnt:
            head = node.next
        else:
            temp = node.next.next
            node.next = temp

        return head
