class Node:
    def __init__(self, prev = None, next = None, key = -1, val = -1):
        self.prev = prev
        self.next = next
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.dummy_head = Node()
        self.dummy_tail = Node()
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

        self.hashmap = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        else:
            node = self.hashmap[key]
            
            if self.dummy_head.next is node:
                return node.val
            else:
                left = node.prev
                right = node.next

                left.next = right
                right.prev = left

                old_front = self.dummy_head.next
                self.dummy_head.next = node
                node.next = old_front
                old_front.prev = node
                node.prev = self.dummy_head

                return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.hashmap:
            new_node = Node(key = key, val = value)
            old_front = self.dummy_head.next
            self.dummy_head.next = new_node
            new_node.next = old_front

            old_front.prev = new_node
            new_node.prev = self.dummy_head

            self.hashmap[key] = new_node

            if len(self.hashmap) == self.capacity + 1:
                old_tail = self.dummy_tail.prev
                self.dummy_tail.prev = old_tail.prev
                old_tail.prev.next = self.dummy_tail

                del self.hashmap[old_tail.key]

        else:
            node = self.hashmap[key]
            node.val = value
            
            if self.dummy_head.next is node:
                return
            else:
                left = node.prev
                right = node.next

                left.next = right
                right.prev = left

                old_front = self.dummy_head.next
                self.dummy_head.next = node
                node.next = old_front
                old_front.prev = node
                node.prev = self.dummy_head



        
