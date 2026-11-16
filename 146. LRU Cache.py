class LRUCache: 
    class Node:
        def  __init__(self, key,val):
            self.key = key
            self.val = val
            self.next = None
            self.prev = None
    
    
    def __init__(self, capacity: int): 
        self.hm = {}
        self.cap = capacity
        self.head = self.Node(None,None)
        self.tail = self.Node(None,None)

        self.head.next = self.tail
        self.tail.prev = self.head 

    def addFirst(self,node):
        currentfirst = self.head.next

        currentfirst.prev = node
        node.next = currentfirst
        
        self.head.next = node
        node.prev = self.head
    def removenode(self,node):
        prinode = node.prev
        nextnode = node.next

        prinode.next = nextnode
        nextnode.prev = prinode
        


    def get(self, key: int) -> int:

        if key not in self.hm:
            return -1
        node = self.hm[key]
        self.removenode(node)
        self.addFirst(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            node = self.hm[key]
            node.val = value
            self.removenode(node)
            self.addFirst(node)
        else:
            if len(self.hm) == self.cap:
                lastnode = self.tail.prev
                self.removenode(lastnode)
                del self.hm[lastnode.key]
            newnode = self.Node(key,value)
            self.addFirst(newnode)
            self.hm[key] = newnode

        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)