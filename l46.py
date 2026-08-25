class LRUCache(object):

    class Node:
        def __init__(self,key=0,val=0):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None
    


    def __init__(self, capacity):
        self.cap = capacity
        self.dict = {}
        self.head = self.Node()
        self.tail = self.Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def addFirst(self,node):
        currfrist = self.head.next

        currfrist.prev = node
        node.next = currfrist

        self.head.next = node
        node.prev = self.head

        self.dict[node.key] = node

    def removeNode(self,node):
        prevnode = node.prev
        nextnode = node.next

        prevnode.next = nextnode
        nextnode.prev = prevnode

        del self.dict[node.key]

    def get(self, key):
        if key not in self.dict:
            return -1
        node = self.dict[key]

        self.removeNode(node)
        self.addFirst(node)

        return node.val

    def put(self, key, value):

        if key in self.dict:
            node = self.dict[key]
            node.val = value
            self.removeNode(node)
            self.addFirst(node)
        else:
            if len(self.dict) == self.cap:
                node =self.tail.prev
                self.removeNode(node)
            node = self.Node(key,value)
            self.addFirst(node)
                

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)