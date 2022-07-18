# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        length = 1
        while node.next:
            node = node.next
            length += 1
        print(length)
        node_p = ListNode(None,head)
        front_node = node_p
        for _ in range(length-n):
            node_p = node_p.next
        node_p.next = node_p.next.next
        return front_node.next