class ListNode:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node

class LinkedList:    
    def __init__(self):
        # Trick: This dummy node makes removing a node
        # from the beginning of the list easier
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head

        while curr and index >= 0:
            curr = curr.next
            index -= 1

        if not curr:
            return -1
        
        return curr.val;

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head.next
        self.head.next = newNode

    def insertTail(self, val: int) -> None:
        curr = self.head
        while curr.next:
            curr = curr.next
        
        newNode = ListNode(val)
        curr.next = newNode
        

    def remove(self, index: int) -> bool:
        curr = self.head

        while curr and index > 0:
            curr = curr.next
            index -= 1

        if curr and curr.next:
            curr.next = curr.next.next
            return True

        return False

    def getValues(self) -> list[int]:
        vals = []

        curr = self.head
        curr = curr.next

        while curr:
            vals.append(curr.val)
            curr = curr.next
        
        return vals

# 1st test case
# LinkedList = LinkedList()
# LinkedList.insertHead(1)
# LinkedList.insertHead(2)
# LinkedList.get(3)

# vals = LinkedList.getValues()
# print(vals)



# 2nd test case
# LinkedList = LinkedList()
# LinkedList.insertHead(1)
# LinkedList.insertTail(2)
# LinkedList.insertHead(0)
# LinkedList.remove(1)

# vals = LinkedList.getValues()
# print(vals)