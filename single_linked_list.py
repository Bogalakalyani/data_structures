class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class SingleLL:
    def __init__(self):
        self.head = None
    def traversal(self):
        n = self.head 
        while n is not None:
            print(f"{n.value} -->", end = " ")
            n = n.next
    def add_empty(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            print("linked list is not empty")
    def add_starting(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    def add_last(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node
    def add_after(self,value,x):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                if n.value == x:
                    break
                n = n.next
            if n is None:
                print("There is no node")
            else:
                new_node = Node(value)
                new_node.next = n.next
                n.next = new_node
    def add_before(self,value,x):
        if self.head is None:
            print("Linked List is empty")
        if self.head.value == x:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                if n.next.value == x:
                    break
                n = n.next
            if n is None:
                print("There is no node")
            else:
                new_node = Node(value)
                new_node.next = n.next
                n.next = new_node
    def delete_begin(self):
        if self.head is None:
            print("linked list is empty")
        else:
            self.head = self.head.next
    def delete_end(self):
        n = self.head
        while n.next.next is not None:
            n = n.next
        n.next = None
    def delete_by_value(self,x):
        if self.head.value == x:
            self.head = self.head.next
        else:
            n = self.head
            while n.next is not None:
                if n.next.value == x:
                    break
                n = n.next
            if n is None:
                print("node is not present")
            else:
                n.next = n.next.next

linked_list = SingleLL()
linked_list.add_empty(10)
linked_list.add_empty(20)
linked_list.add_starting(20)
linked_list.add_starting(30)
linked_list.add_last(40)
linked_list.add_after(100,10)
linked_list.add_before(50,10)
linked_list.delete_begin()
linked_list.delete_end()
linked_list.delete_by_value(50)
linked_list.traversal()
                    




                    
