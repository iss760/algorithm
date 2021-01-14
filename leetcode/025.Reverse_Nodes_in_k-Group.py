# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# k is a positive integer and is less than or equal to the length of the linked list.
# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

# Example:
#   Given this linked list: 1->2->3->4->5
#   For k = 2, you should return: 2->1->4->3->5
#   For k = 3, you should return: 3->2->1->4->5


# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 반환 ListNode 선언
        dummy = ListNode(0)
        dummy.next = head

        cur = dummy     # reverse 첫노드의 전 노드
        while True:
            # reverse 위해 노드들 배치
            temps = []
            temp = cur
            for i in range(k):
                temp = temp.next
                if not temp:
                    return dummy.next
                temps.append(temp)

            # reverse
            temps[0].next = temps[k - 1].next       # 첫노드를 끝노드로
            for i in range(len(temps) - 1, 0, -1):
                temps[i].next = temps[i - 1]
            cur.next = temps[k - 1]                 # 끝노드를 첫노드로

            # reverse 첫노드의 전 노드 재배치
            cur = temps[0]
