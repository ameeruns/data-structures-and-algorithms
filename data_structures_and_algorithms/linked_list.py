class Linkedlist:
    def __init__(self):
        self.head = None
    
    def insert(self,value):
        node = Node(value)
        previous_head = self.head
        self.head = node
        self.head.next = previous_head
    
    def includes(self,value):
        printval = self.head
        status = 'false'
        while printval is not None and printval.value != value:
            printval = printval.next
            node = Node(value)
            self.head = node
        if printval is not None:
            print('ifloop')
            status = 'true'
        return status
    def tostring(self):
        printval = self.head
        tostring_value = ''
        while printval is not None:
            tostring_value = tostring_value + '{' + printval.value + '} -> '
            printval = printval.next
        tostring_value = tostring_value + 'NULL'
        return tostring_value
    def listprint(self):
        printval = self.head
        while printval is not None:
            print (printval.value)
            printval = printval.next

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

copy_list = Linkedlist()

copy_list.head = Node("Apple")
e2 = Node("Banana")
e3 = Node("Orange")

copy_list.head.next = e2
e2.next = e3

#copy_list.listprint()
#status = copy_list.includes('Orange')
#print(status)
#status = copy_list.includes('fruit')
#print(status)
copy_list.insert('animal')
#copy_list.listprint()
#status = copy_list.includes('Bana')
#print(status)
tostring_value = copy_list.tostring()
print(tostring_value)