class Node:
    def __init__(self, key, val):
        self.key = key              # ⚠️ store the key too: eviction needs it to delete from cache
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    # cache: key -> Node, for O(1) lookup
    # list:  left <-> ... <-> right   (left.next = LRU, right.prev = most recent)
    def __init__(self, capacity: int):
        self.cache = {}
        # dummy sentinels, so insert/remove never need edge cases for an empty list
        self.left,self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        self.capacity = capacity

    def remove(self, node):
        # unlink node: its neighbours point at each other
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        # insert just before right = most recent
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            # ⚠️ a read counts as a use: move it to the most recent end
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # ⚠️ unlink the old node first, or it stays in the list as a ghost
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        # ⚠️ evict AFTER inserting; `>` because we're one over capacity now
        if len(self.cache) > self.capacity:
            # ⚠️ save the node first: remove() changes what left.next points to
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

# Time: O(1) for get and put. Space: O(capacity)