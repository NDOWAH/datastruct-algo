class Node:
    '''create a node.
    
    Create a node with given data.
    
    Arg(s): Data values past by the user.
    
    Return: A node containing data.'''

    def __init__(self,data):
        self.data = data
        self.next = next()


class Linkedlist:
    '''Manipulates a node.
    
    Contain methods for mapulating notes e.g adding nodes to a list,
    deleting nodes from list, accessing nodes,counting number of 
    elements from a list.'''

    def __init__(self):
        self.head = None
    
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head
        while self.head is not None:
            current_node = current_node.next
            current_node = Node(value)

    def length(self):
        count = 0
        while self.head is not None:
            count +=1
            self.head = self.head.next

        return count
        

    def display_items(self):
        while self.head is not None:
            print(self.head)
        self.head = self.head.next

    def get_item(self,position):
        pass

        





