# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next: "ListNode" = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr = head
        while True:
            if not curr:
                break
            node = curr.next
            curr.next = prev
            prev = curr
            curr = node
        return prev
