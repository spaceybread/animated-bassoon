# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head == None: return None
        
        le, li = 1, [head]
        
        cur = head
        while cur.next != None:
            cur = cur.next
            le += 1
            li += [cur]

        km = k % le
        nl = li[-km:] + li[:-km]

        out = nl[0]
        cur = out

        for i in range(1, le):
            cur.next = nl[i]
            cur = cur.next
        cur.next = None
        
        return out

        
