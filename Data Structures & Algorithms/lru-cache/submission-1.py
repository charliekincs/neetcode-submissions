class LRUCache:

    head: Entry
    tail: Entry
    cache: dict
    capacity: int
        
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        self._remove(node)
        self._add_to_head(node)
        return node.value


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # assign the value and cut the node from the linked list
            node = self.cache[key]
            node.value = value
            if node == self.head:
                return
            
            self._remove(node)
            # append the node to the end of the linked list as the new head
            self._add_to_head(node)
        elif len(self.cache) == self.capacity:
            del self.cache[self.tail.key]
            self._remove(self.tail)
            self._add_to_head(self.Entry(key, value, None, None))
            self.cache[key] = self.head
        else:
            self._add_to_head(self.Entry(key, value, None, None))
            self.cache[key] = self.head

    def _add_to_head(self, node):
        if self.head is None:
            self.head = self.tail = node
            return
        node.next = None
        node.prev = self.head
        self.head.next = node
        self.head = node


    def _remove(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.tail = node.next
        
        if node.next:
            node.next.prev = node.prev
        else:
            self.head = node.prev

    class Entry:
        key: int
        value: int
        prev: Entry
        next: Entry
        def __init__(self, key, value, prev, next):
            self.key = key
            self.value = value
            self.prev = prev
            self.next = next

