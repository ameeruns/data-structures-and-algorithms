class Linkedlist:
    def __init__(self):
        self.head = None
    
    def insert(self,value):
        node = Node(value)
        self.head = node

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None