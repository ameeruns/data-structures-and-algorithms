from data_structures_and_algorithms.linked_list import Linkedlist, Node


def test_linkedlist_create():
    list_one = Linkedlist()
    assert list_one.head == None

def test_linkedlist_insert():
    list_one = Linkedlist()
    list_one.insert('apples')
    assert list_one.head.value == 'apples'
    assert list_one.head.next == None

def test_linkedlist_insert_two():
    list_one = Linkedlist()
    list_one.head = Node('Apples')
    list_one.head.next = Node('Banana')
    assert list_one.head.value == 'Apples'
    assert list_one.head.next.value == 'Banana'

def test_linkedlist_insert_assignment():
    list_one = Linkedlist()
    list_one.insert('a')
    assert list_one.head.value == 'a'
    assert list_one.head.next == None

def test_linkedlist_insert_assignment1():
    list_one = Linkedlist()
    list_one.head = Node('a')
    list_one.head.next = Node('b')
    b = Node('b') 
    c = Node('c')
    b.next = c
    c.next = None
    assert list_one.head.value == 'a'
    assert list_one.head.next.value == 'b'
    assert b.value == 'b'
    assert b.next.value == 'c'

def test_linkedlist_includes_assignment():
    list_one = Linkedlist()
    list_one.insert('a')
    list_one.insert('b')
    assert list_one.includes('a') == 'true'

def test_linkedlist_includes_f_assignment():
    list_one = Linkedlist()
    list_one.insert('a')
    list_one.insert('b')
    assert list_one.includes('dd') == 'false'

def test_linkedlist_tostring_assignment():
    list_one = Linkedlist()
    list_one.insert('a')
    list_one.insert('b')
    list_one.insert('c')
    assert list_one.tostring() == '{c} -> {b} -> {a} -> NULL'

def test_linkedlist_tostring_one_assignment():
    list_one = Linkedlist()
    list_one.insert('c')
    list_one.insert('b')
    list_one.insert('a')
    assert list_one.tostring() == '{a} -> {b} -> {c} -> NULL'