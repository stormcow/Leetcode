# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        def reconstruct_number(num: ListNode) -> str:
            if not num.next:
                return str(num.val)
            return reconstruct_number(num.next) + str(num.val)

        def link_nums(nums: str) -> ListNode:
            if len(nums) == 1:
                return ListNode(val=int(nums[0]))
            return ListNode(val=int(nums[0]), next=link_nums(nums[1::]))

        num1 = int(reconstruct_number(l1))
        num2 = int(reconstruct_number(l2))
        sum = str(num1 + num2)

        return link_nums(sum[-1::-1])
