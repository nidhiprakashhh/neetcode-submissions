# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head.next == None:
            head = None
            return head

        length = 1
        curr = head
        while curr.next:
            length += 1
            curr = curr.next

        target = length - n

        curr = head

        if n == length:
            return head.next

        for i in range(target - 1):
            curr = curr.next
        
        curr.next = curr.next.next

        return head
        