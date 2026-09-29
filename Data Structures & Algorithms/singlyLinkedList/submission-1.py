class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node(0)
        self.size = 0
    
    def get(self, index: int) -> int:
        if self.size <= index:
            return -1

        curr = self.head.next
        for i in range(index):
            curr = curr.next
        return curr.val

    def insertHead(self, val: int) -> None:
        curr = self.head
        new_node = Node(val)
        new_node.next = curr.next
        curr.next = new_node
        self.size += 1

    def insertTail(self, val: int) -> None:
        curr = self.head
        for i in range(self.size):
            curr = curr.next
        
        new_node = Node(val)
        curr.next = new_node
        self.size += 1

    def remove(self, index: int) -> bool:
        if self.size <= index:
            return False

        curr = self.head
        for i in range(index):
            curr = curr.next
        curr.next = curr.next.next
        self.size -= 1

        return True

    def getValues(self) -> List[int]:
        ans = []
        curr = self.head.next
        for i in range(self.size):
            ans.append(curr.val)
            curr = curr.next

        return ans
