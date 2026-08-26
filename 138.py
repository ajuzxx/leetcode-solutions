"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def addDuplicate(self,head):
        temp = head
        while temp is not None:
            copycat = Node(temp.val)
            copycat.next = temp.next
            temp.next = copycat
            temp =  copycat.next
        return head

    def setupRandom(self,head):
        temp = head
        while temp is not None:
            if temp.random is not None:
                temp.next.random = temp.random.next

            temp = temp.next.next
    def withDrawLL(self,head):
        dummyhead = Node(-1)
        dummytail = dummyhead

        while head is not None:
            dummytail.next=head.next
            head.next=head.next.next
            dummytail = dummytail.next
            head = head.next

        return dummyhead.next




    def copyRandomList(self, head):
       
        # Step1 --> Add duplicate Node
        # Step2 --> Setup Random of DuplicateNode
        # Step3 --> New LinkedList from the DuplicateNodes

        self.addDuplicate(head)

        self.setupRandom(head)

        return self.withDrawLL(head)
        