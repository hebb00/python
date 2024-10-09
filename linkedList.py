class Node:
    def __init__(self, data):
        self.data = data  # Assigns the given data to the node
        self.next = None  # Initialize the next attribute to null

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize head as None
        
    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)  # Create a new node 
        new_node.next = self.head  # Next for new node becomes the   current head
        self.head = new_node  # Head now points to the new node
        
    def printList(self):
        temp = self.head # Start from the head of the list
        while temp:
            print(temp.data,end=' ') # Print the data in the current node
            temp = temp.next # Move to the next node
        print()  # Ensures the output is followed by a new line
    def insertAtEnd(self, new_data):
        new_node = Node(new_data)  # Create a new node
        if self.head is None:
            self.head = new_node  # If the list is empty, make the new node the head
            return
        last = self.head 
        while last.next:  # Otherwise, traverse the list to find the last node
            last = last.next
        last.next = new_node  # Make the new node the next node of the last node
if __name__ == "__main__":
    # Create a new LinkedList instance
    llist = LinkedList()

    # Insert each letter at the beginning using the method we created
    llist.insertAtBeginning('fox') 
    llist.insertAtBeginning('brown') 
    llist.insertAtBeginning('quick')  
    llist.insertAtBeginning('the')  

    # Now 'the' is the head of the list, followed by 'quick', then 'brown' and 'fox'

    # Print the list
    llist.printList()
    list = LinkedList()
    list.insertAtEnd(4)
    list.insertAtEnd(6)
    list.insertAtEnd(8)
    list.printList()