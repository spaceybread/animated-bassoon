# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        if head.val >= 5:
            head = ListNode(1, cur)
        
        while cur != None:
            cur.val = (cur.val << 1) % 10

            if cur.next != None:
                if cur.next.val >= 5:
                    cur.val += 1

            cur = cur.next 
        return head
