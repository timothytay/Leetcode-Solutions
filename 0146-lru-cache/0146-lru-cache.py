class ListNode():
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.val = value
        self.key = None

class LRUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.head = None
        self.tail = self.head
        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            cur = self.cache[key]
            self.removeNode(cur)
            self.addToEnd(cur)
            return cur.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            cur = self.cache[key]
            self.removeNode(cur)
            self.addToEnd(cur)
            cur.val = value
        else:
            if self.size >= self.capacity and key not in self.cache:
                self.cache.pop(self.head.key)
                self.removeFromFront()
            
            self.addToEnd(ListNode(value))
            self.tail.key = key
            self.cache[key] = self.tail

    def removeNode(self, node):
        prev = node.prev
        nxt = node.next
        if prev and nxt:
            prev.next = nxt
            nxt.prev = prev
        elif not prev and not nxt:
            self.head = self.tail = None
        elif not prev:
            self.head = self.head.next
            self.head.prev = None
        elif not nxt:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1

    def addToEnd(self, node):
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            tmp = self.tail
            self.tail = self.tail.next
            self.tail.prev = tmp
        self.size += 1

    def removeFromFront(self):
        if not self.head:
            return
        elif self.size == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)