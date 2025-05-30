class ListNode:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.head, self.tail = ListNode(0), ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.len = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache[key].val
            self.remove(self.cache[key])
            self.insertFront(self.cache[key], self.head)
            return self.cache[key].val[0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = (value, key)
            self.remove(self.cache[key])
            self.insertFront(self.cache[key], self.head)
        else:
            new = ListNode((value, key))
            self.cache[key] = new
            self.insertFront(new, self.head)
            self.len += 1
            if self.len > self.capacity:
                old = self.tail.prev
                self.remove(old)
                self.cache.pop(old.val[1], None)
                self.len -= 1


    def insertFront(self, node: ListNode, head: ListNode) -> None:
        tmp = self.head.next 
        self.head.next = node
        node.prev = self.head
        tmp.prev = node
        node.next = tmp

    def remove(self, node: ListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)