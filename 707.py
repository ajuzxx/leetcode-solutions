class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        self.head = None

    def get(self, index):
        temp = self.head
        count = 0

        while temp:
            if count == index:
                return temp.val

            temp = temp.next
            count += 1

        return -1

    def addAtHead(self, val):
        new = Node(val)
        new.next = self.head
        self.head = new

    def addAtTail(self, val):
        new = Node(val)

        if self.head is None:
            self.head = new
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new

    def addAtIndex(self, index, val):
        if index == 0:
            self.addAtHead(val)
            return

        temp = self.head
        count = 0

        while temp and count < index - 1:
            temp = temp.next
            count += 1

        if temp is None:
            return

        new = Node(val)
        new.next = temp.next
        temp.next = new

    def deleteAtIndex(self, index):
        if self.head is None:
            return

        if index == 0:
            self.head = self.head.next
            return

        temp = self.head
        count = 0

        while temp and count < index - 1:
            temp = temp.next
            count += 1

        if temp is None or temp.next is None:
            return

        temp.next = temp.next.next