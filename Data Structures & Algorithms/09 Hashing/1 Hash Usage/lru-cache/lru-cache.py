"""
LRU Cache (NeetCode)
====================

Implement the Least Recently Used (LRU) cache class LRUCache:
    - LRUCache(int capacity) Initialize the LRU cache of size capacity.
    - int get(int key) Return the value corresponding to the key if the key
      exists, otherwise return -1.
    - void put(int key, int value) Update the value of the key if the key
      exists. Otherwise, add the key-value pair to the cache. If the
      introduction of the new pair causes the cache to exceed its capacity,
      remove the least recently used key.

A key is considered used if a get or a put operation is called on it.

Ensure that get and put each run in O(1) average time complexity.

Example 1:
    Input:
    ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

    Output:
    [null, null, null, 1, null, -1, null, -1, 3, 4]

Constraints:
    1 <= capacity <= 100
    0 <= key <= 1000
    0 <= value <= 1000

Explanation (state after put(3,3) in Example 1, capacity = 2):

    Screenshot: lru-cache.png (in this folder)

    Hash map gives O(1) lookup, doubly linked list gives O(1) reorder/evict.

                    LRU     most recent
                     |           |
        left  <->  [1,1]  <->  [3,3]  <->  right
                     ^           ^
    cache = {        |           |
        1: ----------+           |
        3: ----------------------+
    }

    Node = | key, val |
           | prev | next |

    How it got here:
      put(1,1), put(2,2)  ->  left <-> [1,1] <-> [2,2] <-> right
      get(1)              ->  1 is used, moves to the right end:
                              left <-> [2,2] <-> [1,1] <-> right
      put(3,3)            ->  over capacity, evict left.next = [2,2]:
                              left <-> [1,1] <-> [3,3] <-> right
                              and delete key 2 from cache

    Why store key in Node: on eviction we only have the node (left.next),
    and need its key to delete it from cache.

    Why left/right dummy nodes: insert and remove never have to handle an
    empty list or a missing neighbour.
"""

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