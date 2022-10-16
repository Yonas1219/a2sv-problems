class Node:
    def __init__(self, key = None, val = None, next = None, prev = None):
        self.key, self.val = key, val
        self.next, self.prev = next, prev
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = Node()
        self.tail = Node(prev = self.head)
        self.head.next = self.tail

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        node = self.dic[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.dic:
            if not len(self.dic) < self.capacity:
                del self.dic[self.tail.prev.key]
                self.tail.prev = self.tail.prev.prev
                self.tail.prev.next = self.tail
            self.dic[key] = Node(key, value, self.head.next, self.head)
        else:
            node = self.dic[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = self.head.next
            node.prev = self.head
        self.head.next = self.dic[key]
        self.dic[key].next.prev = self.dic[key]
        self.dic[key].val = value
            
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
