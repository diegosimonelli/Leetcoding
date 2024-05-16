# Create a Node class to create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Method to add a node at begin of LL
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    # Method to add a node at end of LL
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while (current_node.next):
            current_node = current_node.next
        current_node.next = new_node

    # Method to add a node at any index
    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while(current_node != None and position + 1 != index):
                position = position + 1
                current_node = current_node.next
            
            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")

    # Print the size of LL
    def sizeOfLL(self):
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size = size + 1
                current_node = current_node.next
            return size
        else:
            return 0
        
    # Print method for the LL
    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next


# Create new LL
llist = LinkedList()

# Add nodes to the LL
llist.insertAtBegin('a')
llist.insertAtBegin('b')
llist.insertAtBegin('c')
llist.insertAtEnd('d')

# Print the LL or traverse the LL
print("Node Data")
llist.printLL()


# Print size of LL
print("Size of linked list: ")
print(llist.sizeOfLL())