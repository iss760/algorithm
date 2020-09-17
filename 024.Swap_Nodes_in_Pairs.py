# Given a linked list, swap every two adjacent nodes and return its head.
# You may not modify the values in the list's nodes, only nodes itself may be changed.

# Example:
#   Given 1->2->3->4, you should return the list as 2->1->4->3.


# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 반환 ListNode 선언
        dummy = ListNode(0)
        dummy.next = head

        b = p = c = dummy   # swap을 위한 노드
        while c.next:
            # swap을 위해 노드 배치
            c = c.next
            p = p.next.next
            if p is None:
                break

            # swap
            c.next = p.next
            p.next = c
            b.next = p

            # 노드 재배치
            p = p.next
            b = b.next.next

        return dummy.next
