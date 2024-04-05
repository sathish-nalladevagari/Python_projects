class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    

linkedlist =  LinkedList()
linkedlist.head = Node(1)
second = Node(2)
third = Node(3)

linkedlist.prepend(4)



linkedlist.head.next = second
second.next = third

while linkedlist.head != None:
    print(linkedlist.head.data )
    linkedlist.head=linkedlist.head.next