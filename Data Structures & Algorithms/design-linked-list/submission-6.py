class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList:
    # SIMPLE LINKED LIST WITH FOR
    def __init__(self):
        self.head = Node(0)
        self.size = 0

    def is_empty(self):
        return (self.size==0)

    def print_ll(self):
        curr = self.head.next
        for i in range(self.size):
            print(curr.val, end = "=>")
            curr = curr.next
        print()

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1

        curr = self.head.next
        for i in range(index):
            curr = curr.next

        return curr.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        self.size += 1 

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)

        curr = self.head
        for i in range(self.size):
            curr = curr.next    
        curr.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        
        new_node = Node(val)
        curr = self.head

        for i in range(index):
            curr = curr.next

        new_node.next = curr.next
        curr.next = new_node
        self.size += 1 

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return 

        curr = self.head
        for i in range(index):
            curr = curr.next       

        curr.next = curr.next.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)