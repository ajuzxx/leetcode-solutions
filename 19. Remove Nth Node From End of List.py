# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        faster = head
        slower = head

        for i in range(n):
            faster= faster.next
        if faster is None:
            return head.next
        while faster.next != None:
            slower = slower.next
            faster = faster.next
        slower.next = slower.next.next
        return head
        