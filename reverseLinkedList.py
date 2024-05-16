class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
    
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    # T O(n)  M O(1)
    def reverseList(self):
        prev = None
        current_node = self.head

        while current_node:
            nxt = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = nxt
        self.head = prev


    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

llist = LinkedList()

llist.insertAtBegin(1)
llist.insertAtEnd(2)
llist.insertAtEnd(3)
llist.insertAtEnd(4)
llist.insertAtEnd(5)

llist.reverseList()

llist.printLL()